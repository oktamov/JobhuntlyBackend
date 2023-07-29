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
        return self.user.email


class Experience(models.Model):
    class Type(models.TextChoices):
        Part = "part_time"
        Full = "full_time"
        Hybrid = "hybrid"

    class Location(models.TextChoices):
        Remote = "remote"
        On_site = "on site"
        Hybrid = "hybrid"

    title = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, related_name="experiences", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name="experiences", on_delete=models.CASCADE)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    work_type = models.CharField(max_length=100, choices=Type.choices, default=Type.Full)
    location = models.CharField(max_length=100, choices=Location.choices, default=Location.On_site)
    description = models.CharField(max_length=255)


class Education(models.Model):
    student_to = models.DateField()
    student_from = models.DateField()
    gpa = models.IntegerField(default=0)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='education')
    university_id = models.ForeignKey('University', on_delete=models.CASCADE, related_name='university')


class University(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='universities/logo')

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255)


class EmployeeSkill(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="EmployeeSkills")
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="EmployeeSkills")

    class Meta:
        unique_together = ('employee', 'skill')

    def __str__(self):
        return f"{self.employee} - {self.skill}"
