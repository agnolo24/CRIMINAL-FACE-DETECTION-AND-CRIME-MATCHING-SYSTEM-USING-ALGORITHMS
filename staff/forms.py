from django import forms
from . models import *


class staff_registration_form(forms.ModelForm):
    class Meta:
        model = staff
        fields = ['staff_id', 'full_name', 'address', 'contact', 'designation', 'gender', 'date_of_birth']
        widgets = {'staff_id' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'full_name' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'address' : forms.Textarea(attrs={'class' : 'form-control'}),
                   'contact' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'designation' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'gender' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'date_of_birth' : forms.DateInput(attrs={'class' : 'form-control', 'type': 'date'})}
        

class staff_edit_form(forms.ModelForm):
    class Meta:
        model = staff
        fields = ['full_name', 'address', 'contact', 'designation', 'gender', 'date_of_birth']
        widgets = {
                   'full_name' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'address' : forms.Textarea(attrs={'class' : 'form-control'}),
                   'contact' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'designation' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'gender' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'date_of_birth' : forms.DateInput(attrs={'class' : 'form-control', 'type': 'date'})
                   }