from django import forms
from .models import Phonebook

class AddNew(forms.ModelForm):

    class Meta:
        model = Phonebook
        fields=('name','mobile_number','address',)
