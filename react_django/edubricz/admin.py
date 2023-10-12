from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "standrad","roll_no","date_of_birth","phone","gender")
  
admin.site.register(Student, StudentAdmin)


