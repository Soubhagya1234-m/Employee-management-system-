from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Employee
from .forms import EmployeeForm
from .serializers import EmployeeSerializer
# Home
def home(request):
    total_employees = Employee.objects.count()
    context = {
        'total_employees': total_employees,
    }
    return render(
        request,
        'employees/home.html',
        context
    )
# Employee List
def employee_list(request):
    employees = Employee.objects.all().order_by('-id')
    context = {
        'employees': employees,
    }
    return render(
        request,
        'employees/employee_list.html',
        context
    )
# Employee Detail
def employee_detail(request, pk):
    employee = get_object_or_404(
        Employee,
        pk=pk
    )
    context = {
        'employee': employee,
    }
    return render(
        request,
        'employees/employee_detail.html',
        context
    )
# Create Employee
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                'employee_list'
            )
    else:
        form = EmployeeForm()
    context = {
        'form': form,
        'title': 'Add Employee',
    }
    return render(
        request,
        'employees/employee_form.html',
        context
    )
# Update Employee
def employee_update(request, pk):
    employee = get_object_or_404(
        Employee,
        pk=pk
    )
    if request.method == 'POST':
        form = EmployeeForm(
            request.POST,
            instance=employee
        )
        if form.is_valid():
            form.save()
            return redirect(
                'employee_detail',
                pk=employee.pk
            )
    else:
        form = EmployeeForm(
            instance=employee
        )
    context = {
        'form': form,
        'title': 'Update Employee',
    }
    return render(
        request,
        'employees/employee_form.html',
        context
    )
# Delete Employee
def employee_delete(request, pk):
    employee = get_object_or_404(
        Employee,
        pk=pk
    )
    if request.method == 'POST':
        employee.delete()
        return redirect(
            'employee_list'
        )
    context = {
        'employee': employee,
    }
    return render(
        request,
        'employees/employee_confirm_delete.html',
        context
    )
# REST API ViewSet
class EmployeeViewSet(viewsets.ModelViewSet)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer