from django.shortcuts import render, get_object_or_404
from .models import Phonebook
from .forms import AddNew
from django.shortcuts import redirect
from django.core import serializers
from django.http import HttpResponse

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
    
def new_data(request):
    data=JSONParser().parse(request)
    serializer=SnippetSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JSONResponse(serializer.data,status=201)
    return JSONResponse(serializer.errors,status=400)
