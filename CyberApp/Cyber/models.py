import datetime
import time

from django.db import models

# Create your models here.
from django.utils import timezone


class Computers(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    allocate = models.BooleanField(default=False)

    def __str__(self):
        return self.ip_address

class AllocateStudent(models.Model):
    computer = models.ForeignKey(Computers, on_delete=models.CASCADE)
    adm_no = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    check_in = models.DateTimeField(default=datetime.datetime.now())
    check_out = models.DateTimeField(null=True, blank=True)
    reason = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} : {self.computer}'

class AllocateClass(models.Model):
    trainer_name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    course_unit = models.CharField(max_length=50)
    class_size = models.IntegerField()
    class_start = models.DateTimeField(default=datetime.datetime.now())
    class_end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.trainer_name} {self.course_unit}'

class AllocateVisitors(models.Model):
    computer = models.ForeignKey(Computers, on_delete=models.CASCADE)
    visitor_name = models.CharField(max_length=50)
    id_no = models.IntegerField()
    phone_number = models.CharField(max_length=10)
    reason = models.CharField(max_length=100)
    date_of_visit = models.DateField(default=timezone.now)
    time_in = models.TimeField(default=datetime.datetime.now())
    time_out = models.TimeField(null=True, blank=True)
    total_time = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.visitor_name