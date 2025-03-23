from django.urls import path
from . import views

urlpatterns = [
    path('p_data_table/',views.police_station_details_table, name='p_data_table'),
    path('s_data_table/',views.staff_details_table, name='s_data_table'),
    path('accept_s/<str:station_id>', views.accept_s, name='accept_s'),
    path('reject_s/<str:station_id>', views.reject_s, name='reject_s'),
]
