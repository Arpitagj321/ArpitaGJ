from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']

class SignupForm(UserCreationForm):
    pass
