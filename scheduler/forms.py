from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import random, string
from .models import CustomUser, Schedule

def random_code():
    length = 6
    code = ''.join(random.choices(string.ascii_uppercase, k=length))
    print(code)
    return code

class UserRegisterForm(UserCreationForm):

    age = forms.IntegerField()
    email = forms.EmailField()
    unique_id = forms.CharField(max_length=6, required= False, initial = random_code)
    image = forms.FileField(required = False)

    class Meta:
        model = User
        fields = ['username', 'age', 'email', 'password1', 'password2', 'unique_id', 'image']


class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'age', 'email', 'password', 'password_confirm', 'unique_id', 'image']

class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = '__all__'