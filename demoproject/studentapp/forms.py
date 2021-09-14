from django import forms    
from studentapp.models import Student

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        # fields=('name','email','dob','gender','phone')
        fields='__all__'

class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=100, required=False)
    last_name=forms.CharField(max_length=100, required=False)
    email=forms.EmailField()

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
        
