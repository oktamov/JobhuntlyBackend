from django.db import models

from company.models import Company
from users.models import User


class Employee(models.Model):
    class Gender(models.TextChoices):
        MAN = 'man'
        WOMEN = 'women'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employee")
    region = models.CharField(max_length=256, null=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=50, choices=Gender.choices, default=Gender.MAN)

    def __str__(self):
        return self.username.get_full_name()


class Education(models.Model):
    student_to = models.DateField()
    student_from = models.DateField()
    gpa = models.IntegerField(default=0)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='education')
    university_id = models.ForeignKey('University', on_delete=models.CASCADE, related_name='university')


class University(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name
