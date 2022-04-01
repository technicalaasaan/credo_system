from .serializers import DepartmentSearializer, StudentSearializer, StaffSearializer
from .models import Student, Department, Staff
from rest_framework import viewsets


class DepartmentViewSets(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSearializer

class StudentViewSets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSearializer

class StaffViewSets(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSearializer
