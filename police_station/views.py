from django.shortcuts import render, redirect
from . models import *
from . forms import *
from gust . models import login as login_table
from gust . forms import login_form

# Create your views here.


# This function is used for police_station_registration
def police_station_reg_form(request):
    if request.method == 'POST':
        log = login_form(request.POST)
        form = police_station_registration_form(request.POST)
        if form.is_valid() and log.is_valid():
            log_inst=log.save(commit=False)
            log_inst.user_type='station'
            log_inst.save()
            inst=form.save(commit=False)
            inst.login_id=log_inst
            inst.save()
            return redirect('guest_page')
    else:
        form = police_station_registration_form()
        log = login_form()
    return render(request, 'police_station/p_reg_form.html', {'p_reg_form': form, 'log': log})

def station_home(request):
    return render(request, 'police_station/station_home.html')