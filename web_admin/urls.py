from django.urls import path
from . import views

urlpatterns = [
    path('p_data_table/',views.police_station_details_table, name='p_data_table'),
    path('s_data_table/',views.staff_details_table, name='s_data_table'),
]
