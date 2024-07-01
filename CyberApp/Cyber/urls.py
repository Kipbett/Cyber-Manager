from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.computers, name='computers'),
    path('allocated', views.check_out_list, name='allocated'),
    path('checkout/<int:id>/', views.check_out, name='checkout'),
    path('visits', views.student_visit, name='visits'),
    path('classes', views.allocate_class, name='classes'),
    path('allocated-classes', views.allocated_classes, name='allocated-classes'),
    path('checkout-class/<int:id>/', views.end_class, name='checkout-class'),
    path('class-visits', views.class_visits, name='class-visits'),
    path('visitors', views.allocate_visitor, name='visitors'),
    path('allocated-visitors', views.allocated_visitors, name='allocated-visitors'),
    path('checkout-visitor/<int:id>/', views.checkout_visitor, name='checkout-visitor'),
    path('visitor-visits', views.visitors_visit, name='visitor-visits'),
]