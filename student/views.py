from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student, Department
from django.views.decorators.csrf import csrf_exempt
from .forms import SampleForm

# Create your views here.
def home(request):
    data = {'name': request.GET.get('user', 'Credo')}
    return render(request, 'index.html', context={})

def sample(request):
    if request.method == "POST":
        out = SampleForm(request.POST)
        if out.is_valid():
            _data = out.cleaned_data
            resp = Student.objects.create(stu_name= _data['student_name'], stu_age=_data['student_age'], stu_class='1st', address = _data['address'])
            return redirect('/')
        else:
            return HttpResponse('Invalid', status=400)
    else:
        data = SampleForm()
        return render(request, 'sample.html', {'form': data})

def student_form(request):
    if request.method == 'POST':
        _data = StudentForm(request.POST)
        print(_data.is_valid())
        resp = Student.objects.create(**_data.cleaned_data)
        return redirect('/')
    else:
        form_data = StudentForm()
        return render(request, 'sample.html', {'form': form_data})


def staff(request):
    return render(request, 'staff/home.html')

# function based views (FBV)
@csrf_exempt
def student(request):
    if request.method == 'GET':
        age = request.GET.get('age')
        stu_class = request.GET.get('class')
        stu_data = Student.objects.all()
        if age:
            stu_data = stu_data.filter(stu_age__lte=age)
        if stu_class:
            print('st', stu_class)
            stu_data = stu_data.filter(stu_class=stu_class)

        print('stu_data', stu_data)
        return render(request, 'index.html', {'data': stu_data, 'value': range(10) })
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

