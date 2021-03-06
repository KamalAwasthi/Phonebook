from django.shortcuts import render, get_object_or_404
from .models import Phonebook
from .forms import AddNew
import json
from django.shortcuts import redirect
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def contact_list(request):
    contact =Phonebook.objects.all()
    return render(request,'phonebook/contact_list.html',{'contact':contact})

def contact_detail(request,pk):
    contact =get_object_or_404(Phonebook,pk=pk)
    return render(request,'phonebook/contact_detail.html',{'contact':contact})

def Add_New(request):
    if request.method=="POST":    
        form=AddNew(request.POST)
        if form.is_valid():
            post=form.save()
            return redirect('contact_list')
    else:
        form=AddNew()
    return render(request,'phonebook/Add_New.html',{'form':form})

def contact_edit(request,pk):
    contact = get_object_or_404(Phonebook,pk=pk)
    if request.method=="POST":
        form=AddNew(request.POST,instance=contact)
        if form.is_valid():
            contact=form.save()
            return redirect('contact_list')
    else:
        form=AddNew(instance=contact)
    return render(request,'phonebook/Add_New.html',{'form':form})

def contact_delete(request,pk):
    contact=get_object_or_404(Phonebook,pk=pk).delete()
    return redirect('contact_list')

def list(request):
    queryset=Phonebook.objects.all()
    queryset=serializers.serialize('json',queryset)
    return HttpResponse(queryset,content_type="application/json")

@csrf_exempt
def new_data(request):
    data=request.POST
    post=data.get('Json')
    json_dict=json.loads(post)
    m=Phonebook(**json_dict)
    m.save()
    return HttpResponse(str(json_dict))
 
@csrf_exempt       
def delete_object(request):
    data=request.POST
    pk=data.get('pk')
    c=Phonebook.objects.get(pk=pk)
    c.delete()
    return HttpResponse(str(c))
    #c=Phonebook.objects.get(pk=pk)
    #contact.delete()
    #return HttpResponse(str(contact))
