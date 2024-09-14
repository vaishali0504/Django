import random
from django.test import TestCase
from .models import Student


class StudentModelUnitTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            student_number=random.randint(100000000000, 999999999999),
            first_name='Bob',
            last_name='Smith',
            email='bob.smith@test.com',
            field_of_study='Computer Science',
            first_sem=9.99,
            second_sem=9.99,
            third_sem=9.99,
            reappear='physics,chemistry,dsa,wt,math,os,c',
        )

    def test_student_model(self):
        data = self.student
        self.assertIsInstance(data, Student)
