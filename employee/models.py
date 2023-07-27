from django.db import models

from users.models import User
from .managers import CustomUserManager  # noqa


class Employee(CustomUserManager):
    class Gender(models.TextChoices):
        MAN = 'man'
        WOMEN = 'women'

    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employee")
    region = models.CharField(max_length=256, null=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=50, choices=Gender.choices, default=Gender.MAN)

    objects = CustomUserManager()

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.type = 'admin'
        super(Employee, self).save(*args, **kwargs)

    @property
    def full_name(self):
        return self.get_full_name()


class Education(CustomUserManager):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='education')
    university_id = models.ForeignKey('University', on_delete=models.CASCADE, related_name='university')
    student_to = models.DateField()
    student_from = models.DateField()
    gpa = models.IntegerField(default=0)


class University(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name
