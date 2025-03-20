from django.urls import path
from . import views

urlpatterns = [
    path('staff_reg/', views.staff_reg_form, name='staff_reg'),
    path('staff_home/', views.staff_home, name='staff_home'),
    path('staff_profile/', views.staff_profile, name='staff_profile'),
    path('edit_staff_profile/', views.edit_staff_profile, name='edit_staff_profile'),
]
