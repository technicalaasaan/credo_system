from rest_framework import routers
from .viewsets import DepartmentViewSets, StudentViewSets, StaffViewSets

stu_router = routers.DefaultRouter()
stu_router.register(r'department', DepartmentViewSets)
stu_router.register(r'student', StudentViewSets)
stu_router.register(r'staff', StaffViewSets)