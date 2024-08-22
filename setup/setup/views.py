from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from Emp_info.models import Employee

import sys, os
def employee(request):
    try:    
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']

        e=Employee(name=name, email=email, phone=phone, address=address)
        e.save()
    except Exception as e:
        print(e)
        
    return render(request, 'employee.html')


def emsemp(response):
    emp=Employee.objects.all()

    data={
        'emp':emp
    }
    return render(response, 'EMS.html',data)

def addemployee(request):
    try:    
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']

        e=Employee(name=name, email=email, phone=phone, address=address)
        e.save()
        return redirect("/emsemp")
    except Exception as e:
        print(e)

def updateemployee(request,id):
    try:    
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']

        e=Employee(id=id, name=name, email=email, phone=phone, address=address)
        e.save()
        return redirect("/emsemp")
    except Exception as e:
        print(e)

def deleteemployee(request,id):
    Employee.objects.filter(id=id).delete()
    
    return redirect("/emsemp")
    
    
