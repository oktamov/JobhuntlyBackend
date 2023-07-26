from django.db import models

from users.models import User
from .managers import CustomUserManager


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
