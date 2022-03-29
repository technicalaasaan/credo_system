from django.shortcuts import render
from django.http import HttpResponse
from .form import StudentForm
from django.contrib.auth.models import User
from django.views.generic.list import ListView
# Create your views here.
def home(request):
    return HttpResponse('Hi Hello! Welcome You All!')

def student(request):
    form = StudentForm()
    return render(request, 'student.html', {'data': form})

class User(ListView):
    model = User
