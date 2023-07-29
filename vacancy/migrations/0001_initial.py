# Generated by Django 4.2.3 on 2023-07-28 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('employee', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('experience', models.CharField(max_length=255)),
                ('level', models.CharField(choices=[('Internship', 'Internship'), ('Junior', 'Junior'), ('Middle', 'Middle'), ('Senior', 'Senior')], default='Junior', max_length=10)),
                ('job_type', models.CharField(choices=[('full time', 'full time'), ('part time', 'part time')], default='part time', max_length=10)),
                ('salary', models.IntegerField(default=0)),
                ('overview', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('offer', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='employee.employee')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='vacancy.vacancy')),
            ],
            options={
                'unique_together': {('employee', 'vacancy')},
            },
        ),
    ]