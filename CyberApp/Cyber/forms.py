from django import forms

from .models import AllocateStudent, AllocateClass, AllocateVisitors


class AllocateStudentForm(forms.ModelForm):
    class Meta:
        model = AllocateStudent
        fields = ['name', 'adm_no', 'computer', 'reason']


class AllocateClassForm(forms.ModelForm):
    class Meta:
        model = AllocateClass
        fields = ['trainer_name', 'course', 'course_unit', 'class_size']


class AllocateVisitorForm(forms.ModelForm):
    class Meta:
        model = AllocateVisitors
        fields = ['visitor_name', 'id_no', 'phone_number', 'reason', 'computer']
