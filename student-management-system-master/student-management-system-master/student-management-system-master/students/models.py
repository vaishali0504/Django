from django.db import models


# Create your models here.
class Student(models.Model):
  student_number = models.PositiveIntegerField()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  field_of_study = models.CharField(max_length=50)
  first_sem = models.FloatField()
  second_sem = models.FloatField()
  third_sem = models.FloatField()
  reappear = models.CharField(max_length=150)
  
  
  

  def __str__(self):
    return f'Student: {self.first_name} {self.last_name}'
