from django.db import models


class University(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='universities/logo')

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255)
