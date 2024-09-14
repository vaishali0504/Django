from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'first_sem', 'second_sem', 'third_sem','reappear']
    labels = {
      'student_number': 'Student Number',
      'first_name': 'First Name',
      'last_name': 'Last Name',
      'email': 'Email',
      'field_of_study': 'Field of Study',
      'first_sem': 'FIRST SEM',
      'second_sem': 'SECOND SEM',
      'third_sem': 'THIRD SEM',
      'reappear': 'REAPPEAR',


    }
    widgets = {
      'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
      'first_sem': forms.NumberInput(attrs={'class': 'form-control'}),
      'second_sem': forms.NumberInput(attrs={'class': 'form-control'}),
      'third_sem': forms.NumberInput(attrs={'class': 'form-control'}),
      'reappear': forms.TextInput(attrs={'class': 'form-control'}),
    }
