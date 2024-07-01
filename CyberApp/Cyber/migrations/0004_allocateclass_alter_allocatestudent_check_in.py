# Generated by Django 5.0.6 on 2024-06-14 17:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cyber', '0003_alter_allocatestudent_check_in'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllocateClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('course_unit', models.CharField(max_length=50)),
                ('class_size', models.IntegerField()),
                ('class_start', models.DateTimeField(default=datetime.datetime(2024, 6, 14, 20, 30, 44, 733688))),
                ('class_end', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='allocatestudent',
            name='check_in',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 14, 20, 30, 44, 733688)),
        ),
    ]
