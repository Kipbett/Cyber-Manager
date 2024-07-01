import datetime
import time

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.utils import timezone

from .forms import AllocateStudentForm, AllocateClassForm, AllocateVisitorForm
from .models import Computers, AllocateStudent, AllocateClass, AllocateVisitors


def computers(request):
    comps = Computers.objects.filter(allocate=False)
    form = AllocateStudentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            id = request.POST['computer']
            update_comp = get_object_or_404(Computers, id=id)
            update_comp.allocate=True
            update_comp.save()
            form.save()
            return redirect('allocated')
        else:
            form = AllocateStudentForm(request.POST)

    return render(request, 'home.html', {'computers': comps, 'form': form})

def allocate_class(request):
    form = AllocateClassForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('allocated-classes')
        else:
            form = AllocateClassForm(request.POST)

    return render(request, 'classes.html', {'form': form})

def allocated_classes(request):
    allocated_class = AllocateClass.objects.filter(class_end__isnull=True)
    return render(request, 'allocated-classes.html', {'allocated_classes': allocated_class})

def end_class(request, id):
    end_class = get_object_or_404(AllocateClass, id=id, class_end__isnull=True)
    end_class.class_end = datetime.datetime.now()
    end_class.save()
    return redirect('allocated-classes')

def check_out_list(request):
    allocated_comps = AllocateStudent.objects.filter(check_out__isnull=True)
    return render(request, 'check-out.html', {'allocated': allocated_comps})

def class_visits(request):
    class_visits = AllocateClass.objects.filter(class_end__isnull=False)
    return render(request, 'class-visits.html', {'class_visits': class_visits})

def check_out(request, id):
    checkout = get_object_or_404(AllocateStudent, id=id, check_out__isnull=True)
    checkout.check_out = datetime.datetime.now()
    checkout.save()
    return redirect('allocated')

def student_visit(request):
    visits = AllocateStudent.objects.filter(check_out__isnull=False)
    return render(request, 'student-visit.html', {'visits': visits})

def allocate_visitor(request):
    visitor_computers = Computers.objects.filter(allocate=False)
    form = AllocateVisitorForm(request.POST)
    if form.is_valid():
        id = request.POST['computer']
        update_comp = get_object_or_404(Computers, id=id)
        update_comp.allocate = True
        update_comp.save()
        form.save()
        return redirect('allocated-visitors')
    else:
        form = AllocateVisitorForm(request.POST)

    return render(request, 'visitors.html', {'computers': visitor_computers, 'form': form})

def allocated_visitors(request):
    visitors = AllocateVisitors.objects.filter(time_out__isnull=True)
    return render(request, 'allocated-visitors.html', {'visitors': visitors})

def checkout_visitor(request, id):
    checkout_visit = get_object_or_404(AllocateVisitors, id=id, time_out__isnull=True)
    checkout_visit.time_out = timezone.localtime()
    # checkout_visit.total_time = checkout_visit.time_in - checkout_visit.time_out
    checkout_visit.save()
    return redirect('allocated-visitors')

def visitors_visit(request):
    visitors_visits = AllocateVisitors.objects.filter(time_out__isnull=False)
    return render(request, 'visitors-visit.html', {'visitors_visits': visitors_visits})


