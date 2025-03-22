from django.urls import path
from . import views

urlpatterns = [
    path('user_reg/', views.user_reg, name='user_reg'),
    path('user_home/', views.user_home, name='user_home'),
]
