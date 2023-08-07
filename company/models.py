from django.db import models

from users.models import User


class Benefit(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    logo = models.ImageField('companies/logo/')
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE, related_name='benefits', null=True)

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=256)
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE, related_name='sectors', null=True)

    def __str__(self):
        return self.name


class TechStack(models.Model):
    logo = models.ImageField('companies/contact/logo/', null=True, blank=True)
    name = models.CharField(max_length=32)
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE, related_name='tech_stacks', null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    class ContactChoices(models.TextChoices):
        facebook = 'facebook', 'Facebook'
        twitter = 'twitter', 'Twitter'
        linkedin = 'linkedin', 'LinkedIn'
        mailbox = 'mailbox', 'Mailbox'

    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE, related_name='contacts', null=True)
    company = models.ForeignKey('Company', models.CASCADE, related_name='contacts')
    url = models.URLField()
    contact = models.CharField(max_length=10, choices=ContactChoices.choices)

    def __str__(self):
        return self.company.name


class WorkingAtCompany(models.Model):
    company = models.ForeignKey('Company', models.CASCADE, 'images')
    image = models.ImageField(upload_to='companies/WorkingImages/', null=True, blank=True)
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE, related_name='working_company', null=True)

    def __str__(self):
        return self.company.name + ' ' + self.image.name


class Company(models.Model):
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE, related_name='companies', null=True)
    name = models.CharField(max_length=128)
    region = models.CharField(max_length=64)
    location = models.CharField(max_length=256)
    description = models.TextField()
    size = models.CharField(max_length=32)
    revenue = models.CharField(max_length=32)
    founded = models.DateField()
    logo = models.ImageField(upload_to='companies/logo/', null=True, blank=True)
    sector = models.ForeignKey(to=Sector, on_delete=models.CASCADE, related_name='companies', null=True)
    benefits = models.ManyToManyField(to=Benefit, related_name='companies', null=True, blank=True)
    tech_stacks = models.ManyToManyField(to=TechStack, related_name='companies', null=True, blank=True)
    job_count = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def jobs_count(self):
        return self.vacancies.count()

    def __str__(self):
        return self.name
