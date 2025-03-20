from django.urls import path
from . import views

urlpatterns = [
    path('', views.guest_page, name='guest_page'),
    path('login_form/', views.login_check, name='login_form'),

]
