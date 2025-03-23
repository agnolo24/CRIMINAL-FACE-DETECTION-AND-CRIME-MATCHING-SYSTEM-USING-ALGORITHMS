from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from . forms import *
from gust . models import login as login_table
from gust . forms import login_form


# Create your views here.


# This function is used for staff_registration
def staff_reg_form(request):
    if request.method == 'POST':
        log = login_form(request.POST)
        form = staff_registration_form(request.POST)
        if form.is_valid() and log.is_valid():
            log_inst=log.save(commit=False)
            log_inst.user_type='staff'
            log_inst.varification_status = 'varified'
            log_inst.save()
            inst=form.save(commit=False)
            inst.login_id=log_inst
            inst.save()
            return redirect('login_form')
    else:
        form = staff_registration_form()
        log = login_form()
    return render(request, 'staff/s_reg_form.html', {'s_reg_form': form, 'log': log})

def staff_home(request):
    return render(request, 'staff/staff_home.html')

# To view the staff profile after the login
def staff_profile(request):
    staff_id = request.session.get('staff_id')
    log_staf = get_object_or_404(login_table, id = staff_id)    
    data = staff.objects.get(login_id = log_staf)
    return render(request, 'staff/staff_profile.html', {'data' : data})

# To edit the staff data after login
def edit_staff_profile(request):
    staff_id = request.session.get('staff_id')
    log_staf = get_object_or_404(login_table, id = staff_id)
    data = staff.objects.get(login_id = log_staf)
    if request.method == 'POST':
        form = staff_edit_form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('staff_profile')
    else:
        form = staff_edit_form(instance=data)
    return render(request, 'staff/edit_staff.html', {'form' : form})