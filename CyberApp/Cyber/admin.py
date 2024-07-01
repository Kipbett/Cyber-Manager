from django.contrib import admin

# Register your models here.
from .models import Computers, AllocateStudent, AllocateClass, AllocateVisitors

admin.site.register(Computers)
admin.site.register(AllocateStudent)
admin.site.register(AllocateClass)
admin.site.register(AllocateVisitors)