"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from student.urls import stu_router
from student.views import home, staff, student_form, sample, student, StudentView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('', student),
    path('staff/', staff),
    # path('sample/', sample), #basic form
    path('sample/', student_form), #model form
    path('student_func/', student), # function based
    path('student/', StudentView.as_view()), # List View
    path('student/<pk>/', StudentDetailView.as_view()), # Detail View
    path('student_add/', StudentCreateView.as_view()),
    path('student/<pk>/update/', StudentUpdateView.as_view()),
    path('student/<pk>/delete/', StudentDeleteView.as_view()),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('clg/', include(stu_router.urls)),
]