from django.contrib import admin
from employee.models import Employee# Register your models here.


class Emp_display(admin.ModelAdmin):
    list_display = ['name', 'designation', 'email', 'created_at']
    search_fields = ('name', )  # by this we can search by name in admin panel on db


admin.site.register(Employee, Emp_display) #it Employee displays the table created whereas Emp_display will display the fields on the outer side of the Employee table