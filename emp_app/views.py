from django.shortcuts import render,HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request,'all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['n1']
        last_name = request.POST['n2']
        salary = request.POST['n3']
        bonus = request.POST['n4']
        phone = request.POST['n5']
        role = request.POST['n6']
        dept = request.POST['n7']
        location = request.POST['n8']
        hire_date = request.POST['n9']
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, role_id=role, dept_id=dept, location=location, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully")
    elif request.method == 'GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse("An Exception Occured! Employee has not been added successfully")

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed successfully")
        except:
            return HttpResponse("please enter a valid emp id")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['n1']
        dept = request.POST['n7']
        role = request.POST['n6']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request,'all_emp.html',context)
    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')


