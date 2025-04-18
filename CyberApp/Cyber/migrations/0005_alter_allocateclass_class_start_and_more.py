# Generated by Django 5.0.6 on 2024-06-15 17:51

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cyber', '0004_allocateclass_alter_allocatestudent_check_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocateclass',
            name='class_start',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 15, 20, 51, 45, 260512)),
        ),
        migrations.AlterField(
            model_name='allocatestudent',
            name='check_in',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 15, 20, 51, 45, 260512)),
        ),
        migrations.CreateModel(
            name='AllocateVisitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=50)),
                ('id_no', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('reason', models.CharField(max_length=100)),
                ('time_in', models.DateTimeField(default=datetime.datetime(2024, 6, 15, 20, 51, 45, 265541))),
                ('time_out', models.DateTimeField(blank=True, null=True)),
                ('total_time', models.IntegerField(blank=True, null=True)),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cyber.computers')),
            ],
        ),
    ]
