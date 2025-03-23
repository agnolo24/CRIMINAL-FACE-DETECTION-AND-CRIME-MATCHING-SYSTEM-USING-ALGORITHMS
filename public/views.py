from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . models import *
from . forms import *
from police_station . models import police_station_registration
from gust . models import login as login_table
from gust . forms import login_form


# Create your views here.


# This function is used for user(public) registration
def user_reg(request):
    if request.method == 'POST':
        form = user_registration_form(request.POST)
        log = login_form(request.POST)
        if form.is_valid() and log.is_valid():
            log_ins = log.save(commit=False)
            log_ins.user_type = 'user'
            log_ins.varification_status = 'varified'
            log_ins.save()
            form_ins = form.save(commit=False)
            form_ins.login_id = log_ins
            form_ins.save()
            return redirect('guest_page')
    else:
        form = user_registration_form()
        log = login_form()
    return render(request, 'public/user_registration_form.html', {'form' : form, 'log' : log})

def user_home(request):
    return render(request, 'public/user_home.html')

def user_profile(request):
    user_id=request.session.get('user_id')
    log_user=get_object_or_404(login_table,id=user_id)
    data=user_registration.objects.get(login_id=log_user)
    return render(request,'public/public_profile.html',{'data':data})

def user_profile_edit(request):
    user_id=request.session.get('user_id')
    log_user=get_object_or_404(login_table,id=user_id)
    data=user_registration.objects.get(login_id=log_user)
    if request.method=='POST':
        form=user_registration_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form=user_registration_form(instance=data)
    return render(request,'public/public_edit.html',{'form':form})

def search_station(request):
    if request.method == 'POST':
        form = search_station_form(request.POST)
        if form.is_valid():
            station_id = form.cleaned_data['Station_id']
            try:
                station = get_object_or_404(police_station_registration, station_id = station_id)
                login_info = login_table.objects.get(id = station.login_id.id)
                if login_info.varification_status == 'varified':
                    return render(request, 'public/station_search_result.html', {'station' : station})
                else:
                    messages.error(request, 'police station is not varified')
            except police_station_registration.DoesNotExist:
                messages.error(request, 'Police station does not exist')    
    else:
        form = search_station_form()
    return render(request, 'public/search_station.html', {'form' : form})