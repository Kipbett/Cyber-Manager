# Generated by Django 5.0.6 on 2024-06-22 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cyber', '0016_alter_allocateclass_class_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocateclass',
            name='class_start',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 22, 20, 10, 24, 710072)),
        ),
        migrations.AlterField(
            model_name='allocatestudent',
            name='check_in',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 22, 20, 10, 24, 710072)),
        ),
        migrations.AlterField(
            model_name='allocatevisitors',
            name='date_of_visit',
            field=models.DateField(default=datetime.datetime(2024, 6, 22, 17, 10, 24, 725107, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='allocatevisitors',
            name='time_in',
            field=models.TimeField(default=datetime.time),
        ),
    ]
