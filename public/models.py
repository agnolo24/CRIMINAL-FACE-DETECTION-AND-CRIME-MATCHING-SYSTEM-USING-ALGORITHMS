from django.db import models
from gust . models import login

# Create your models here.


class user_registration(models.Model):
    login_id = models.ForeignKey(login, on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(max_length=30)
    contact = models.CharField(max_length=20)