from .models import Department, Student, Staff
from rest_framework import serializers

class DepartmentSearializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class StudentSearializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class StaffSearializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"
