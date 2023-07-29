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


class TechStack(models.Model):
    logo = models.ImageField('companies/contact/logo/')
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Contact(models.Model):
    class ContactChoices(models.TextChoices):
        facebook = 'facebook', 'Facebook'
        twitter = 'twitter', 'Twitter'
        linkedin = 'linkedin', 'LinkedIn'
        mailbox = 'mailbox', 'Mailbox'

    company = models.ForeignKey('Company', models.CASCADE, related_name='contacts')
    url = models.URLField()
    contact = models.CharField(max_length=10, choices=ContactChoices.choices)

    def __str__(self):
        return self.company.name


class WorkingAtCompany(models.Model):
    company = models.ForeignKey('Company', models.CASCADE, 'images')
    image = models.ImageField(upload_to='companies/WorkingImages/')

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
    logo = models.ImageField(upload_to='companies/logo/')
    sector = models.ForeignKey(to=Sector, on_delete=models.CASCADE, related_name='companies')
    benefits = models.ManyToManyField(to=Benefit, related_name='companies')
    tech_stacks = models.ManyToManyField(to=TechStack, related_name='companies')

    def __str__(self):
        return self.name
