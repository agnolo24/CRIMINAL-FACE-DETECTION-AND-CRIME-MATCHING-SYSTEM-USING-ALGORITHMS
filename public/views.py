from django.shortcuts import render, redirect
from . models import *
from . forms import *
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