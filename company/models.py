from django.db import models


class Benefit(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    logo = models.ImageField('companies/logo/')

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Company(models.Model):
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE, related_name='companies')
    name = models.CharField(max_length=128)
    region = models.CharField(max_length=64)
    location = models.CharField(max_length=256)
    description = models.TextField()
    size = models.CharField(max_length=32)
    revenue = models.CharField(max_length=32)
    founded = models.DateField()
    logo = models.ImageField(upload_to='companies/logo/')
    sector = models.ForeignKey(to=Sector, on_delete=models.CASCADE, related_name='companies')
    benefits = models.ManyToManyField(to=Benefit, related_name='companies')

    def __str__(self):
        return self.name
