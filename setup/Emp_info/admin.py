from django.contrib import admin
from Emp_info.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','address')

admin.site.register(Employee,EmployeeAdmin)
