# Generated by Django 5.0.6 on 2024-07-14 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cyber', '0019_alter_allocateclass_class_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocateclass',
            name='class_start',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 14, 13, 26, 42, 274091)),
        ),
        migrations.AlterField(
            model_name='allocatestudent',
            name='check_in',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 14, 13, 26, 42, 274091)),
        ),
        migrations.AlterField(
            model_name='allocatevisitors',
            name='time_in',
            field=models.TimeField(default=datetime.datetime(2024, 7, 14, 13, 26, 42, 274091)),
        ),
    ]
