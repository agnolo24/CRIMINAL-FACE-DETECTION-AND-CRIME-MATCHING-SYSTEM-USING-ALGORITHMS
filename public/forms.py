from django import forms
from . models import *


class user_registration_form(forms.ModelForm):
    class Meta:
        model = user_registration
        fields = ['fullname', 'contact']