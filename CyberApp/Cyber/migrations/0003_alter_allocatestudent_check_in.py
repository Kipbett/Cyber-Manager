# Generated by Django 5.0.6 on 2024-06-14 17:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cyber', '0002_allocatestudent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocatestudent',
            name='check_in',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 14, 20, 17, 42, 4039)),
        ),
    ]