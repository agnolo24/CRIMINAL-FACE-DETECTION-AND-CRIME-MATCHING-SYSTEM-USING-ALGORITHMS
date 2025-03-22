from django.urls import path, include
from . import views

urlpatterns = [
    path('police_station_reg_form/', views.police_station_reg_form, name='police_station_reg_form'),
    path('station_home/', views.station_home, name='station_home'),
    path('station_profile/', views.station_profile, name='station_profile'),
    path('edit_station_profile/', views.edit_station_profile, name='edit_station_profile'),
]
