from django import forms
from . models import *


class user_registration_form(forms.ModelForm):
    class Meta:
        model = user_registration
        fields = ['fullname', 'contact']
        widgets = {
            'fullname' : forms.TextInput(attrs={'class' : 'form-control'}),
            'contact' : forms.TextInput(attrs={'class' : 'form-control'})
        }


class search_station_form(forms.Form):
    Station_id = forms.CharField()
