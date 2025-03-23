from django.shortcuts import render, redirect, get_object_or_404
from police_station . models import police_station_registration
from staff . models import staff
from gust . models import login
from . models import *

# Create your views here.


# This is the function for showing the details of the police station we registred (used for admin)
def police_station_details_table(request):
    police_station_data = police_station_registration.objects.all()
    return render(request, 'web_admin/data.html',{'data1':police_station_data})

# This is the function for showing the details of the staff we registred (used for admin)
def staff_details_table(request):
    staff_data = staff.objects.all()
    return render(request, 'web_admin/data_staff.html',{'Datas':staff_data})

def accept_s(request, station_id):
    station = get_object_or_404(login, id = station_id)
    station.varification_status = 'varified'
    station.save()
    return redirect('p_data_table')

def reject_s(request, station_id):
    station = get_object_or_404(login, id = station_id)
    station.varification_status = 'reject'
    station.save()
    return redirect('p_data_table')

