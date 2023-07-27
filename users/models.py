from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import AccountManager


class User(AbstractUser):
    username = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = AccountManager()

    def __str__(self):
        if self.first_name:
            return self.get_full_name()
        return self.pk
