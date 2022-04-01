from django.contrib import admin
from .models import Student, Department, Subject, Examination, Staff
# Register your models here.
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Examination)
admin.site.register(Staff)