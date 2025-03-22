from django import forms
from . models import police_station_registration


class police_station_registration_form(forms.ModelForm):
    class Meta:
        model = police_station_registration
        fields = ['station_id', 'address_line_1', 'address_line_2', 'district', 'city', 'contact']


class edit_station_profile_form(forms.ModelForm):
    class Meta:
        model = police_station_registration
        fields = ['address_line_1', 'address_line_2', 'district', 'city', 'contact']