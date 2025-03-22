from django.shortcuts import render, redirect, get_object_or_404
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

def station_profile(request):
    station_id = request.session.get('station_id')
    log_station = get_object_or_404(login_table, id = station_id)
    data = police_station_registration.objects.get(login_id = log_station)
    return render(request, 'police_station/station_profile.html', {'data' : data})

def edit_station_profile(request):
    station_id = request.session.get('station_id')
    log_station = get_object_or_404(login_table, id = station_id)
    data = police_station_registration.objects.get(login_id = log_station)
    if request.method == 'POST':
        form = edit_station_profile_form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('station_profile')
    else:
        form = edit_station_profile_form(instance=data)
    return render(request, 'police_station/edit_station_profile.html', {'form' : form})