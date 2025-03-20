from django.db import models
from gust . models import login

# Create your models here.


class police_station_registration(models.Model):
    station_id = models.CharField(max_length=100, primary_key=True)
    login_id = models.ForeignKey(login, on_delete=models.CASCADE, null=True, blank=True)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)