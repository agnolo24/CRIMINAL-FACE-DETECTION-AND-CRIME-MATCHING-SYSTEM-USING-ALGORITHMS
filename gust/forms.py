from django import forms
from . models import *


class login_form(forms.ModelForm):
    class Meta:
        model = login
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'type': 'password'})
        }


class Login_check_form(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()