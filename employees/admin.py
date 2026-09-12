from django.contrib import admin
from .models import Employee
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'phone',
        'department',
        'designation',
        'salary',
        'joining_date',
    )
    search_fields = (
        'name',
        'email',
        'department',
        'designation',
    )
    list_filter = (
        'department',
        'designation',
    )