from django import forms
from .models import Student


class SampleForm(forms.Form):
    student_name = forms.CharField(max_length=70)
    student_age = forms.IntegerField()
    address = forms.CharField(widget=forms.Textarea)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'stu_name': forms.TextInput(attrs= {'placeholder': 'Enter your Name:', 'class': 'form-control'}),
            'stu_dept': forms.RadioSelect(attrs={'class': 'form-check'}),
            'stu_class': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'})
        }