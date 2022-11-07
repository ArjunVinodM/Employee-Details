from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('all_emp.html', views.all_emp, name='all_employee'),
    path('add_emp.html', views.add_emp, name='add_employee'),
    path('add_emp', views.add_emp, name='adding_employee'),
    path('remove_emp.html', views.remove_emp, name='remove_employee'),
    path('remove_emp/<int:emp_id>', views.remove_emp, name='remove_employee'),
    path('filter_emp.html', views.filter_emp, name='filter_employee'),
    path('filter_emp', views.filter_emp, name='filter_employee'),
    path('index', views.index, name='back_space'),
]