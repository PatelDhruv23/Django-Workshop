from django.forms import ModelForm
from .models import student

class StudentForm(ModelForm):
    class Meta:
        model = student
        field = ["sname","smobile","semail","spassword"]
        exclude = ['createdAt']
        #fields = '__all__'