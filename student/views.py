from django.shortcuts import render
from django.http import HttpResponse
from .form import StudentForm
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student, Department
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'index.html')

# function based views (FBV)
@csrf_exempt
def student(request):
    if request.method == 'GET':
        print(request.GET.get('age'))
        age = request.GET.get('age')
        if age:
            stu_data = Student.objects.filter(stu_age=request.GET.get('age'))
        else:
            stu_data = Student.objects.all()
        print('stu_data', stu_data)
        return render(request, 'student.html', {'data': stu_data})
    elif request.method == 'POST':
        data = eval(request.body)
        dept = Department.objects.get(dept_name=data['stu_dept'])
        data.update({'stu_dept': dept})
        resp = Student.objects.create(**data)
        print('resp', resp)
        return HttpResponse('Success!')


# View,
# ListView
# DetailView
# CreateView
# UpdateView
# DeleteView

class StudentView(ListView):
    model = Student
    template_name = 'student.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_list.html'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_form.html'
    fields = ['stu_name', 'stu_age', 'stu_dept', 'stu_class', 'address']
    success_url = '/'

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student_form.html'
    fields = ['stu_age', 'stu_class', 'address']
    success_url = '/'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_delete.html'
    fields = ['stu_age', 'stu_class', 'address']
    success_url = '/'

