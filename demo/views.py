from django.shortcuts import render
from employee.models import Employee

def home(request):
    employee_data = Employee.objects.all().order_by('-name') #Employee is from modals.py of the employee app # order_by fun will display the order according to the given field and - represents descending order
    context = {
        "employee":employee_data,
    }
    return render(request, 'home.html', context)

