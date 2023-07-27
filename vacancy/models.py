from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Vacancy(models.Model):
    LEVEL_CHOICES = (
        ('Junior', 'Junior'),
        ('Middle', 'Middle'),
        ('Senior', 'Senior'),
    )
    JOB_TYPE_CHOICES = (
        ('full time', 'full time'),
        ('part time', 'part time'),
    )
    title = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='Junior')
    job_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES, default='part time')
    salary = models.IntegerField(default=0)
    overview = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    offer = models.TextField(blank=True, null=True)
    # company = models.ForeignKey("Company", related_name="vacancies", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="vacancies", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
