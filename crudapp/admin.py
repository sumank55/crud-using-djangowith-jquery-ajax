from django.contrib import admin
from .models import StudentData

# Register your models here.
@admin.register(StudentData)
class StudentDataAdmin(admin.ModelAdmin):
    list_display=('id', 'name','email','gender','created_at')
