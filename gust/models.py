from django.db import models

# Create your models here.


class login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    user_type = models.CharField(max_length =50)