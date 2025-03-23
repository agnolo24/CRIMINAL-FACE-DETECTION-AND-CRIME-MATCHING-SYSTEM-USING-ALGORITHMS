from django.urls import path
from . import views

urlpatterns = [
    path('user_reg/', views.user_reg, name='user_reg'),
    path('user_home/', views.user_home, name='user_home'),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('user_profile_edit/',views.user_profile_edit,name='user_profile_edit'),
    path('search_station/', views.search_station, name='search_station',)
]
