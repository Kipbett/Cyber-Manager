# Generated by Django 5.0.6 on 2024-06-22 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cyber', '0015_alter_allocateclass_class_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocateclass',
            name='class_start',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 22, 20, 8, 3, 855313)),
        ),
        migrations.AlterField(
            model_name='allocatestudent',
            name='check_in',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 22, 20, 8, 3, 855313)),
        ),
        migrations.AlterField(
            model_name='allocatevisitors',
            name='date_of_visit',
            field=models.DateField(default=datetime.datetime(2024, 6, 22, 17, 8, 3, 855313, tzinfo=datetime.timezone.utc)),
        ),
    ]
