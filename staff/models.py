from django.db import models
from gust . models import login

# Create your models here.


class staff(models.Model):
    staff_id = models.CharField(max_length=50, primary_key=True)
    login_id = models.ForeignKey(login, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    date_of_birth = models.CharField(max_length=20)