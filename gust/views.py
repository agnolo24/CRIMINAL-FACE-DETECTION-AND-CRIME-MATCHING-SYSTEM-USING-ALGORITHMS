from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . models import login as login_table
from . forms import *

# Create your views here.


def guest_page(request):
    return render(request, 'guest/guest_page.html')

# This function is used for login(using this function login can be done by all three users station, staff, user(public))
def login_check(request):
    if request.method == 'POST':
        form = Login_check_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(email, password)
            try:
                user = get_object_or_404(login_table, email=email)
                if user.password == password:
                    if user.user_type == 'station':
                        request.session['station_id'] = user.id
                        return redirect('station_home')
                    elif user.user_type == 'staff':
                        request.session['staff_id'] = user.id
                        return redirect('staff_home')
                    elif user.user_type == 'user':
                        request.session['user_id'] = user.id
                        return redirect('user_home')
                else:
                    messages.error(request, 'Invalid password')
            except login_form.DoesNotExist:
                messages.error(request, 'User does not exist')
    else:
        form = Login_check_form()
    return render(request, 'guest/login.html', {'login_form': form})