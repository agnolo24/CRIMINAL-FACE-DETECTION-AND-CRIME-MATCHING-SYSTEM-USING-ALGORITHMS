# Generated by Django 5.1.2 on 2025-03-23 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('police_station', '0002_police_station_registration_varification_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='police_station_registration',
            name='varification_status',
        ),
    ]
