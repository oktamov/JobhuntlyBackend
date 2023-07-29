# Generated by Django 4.2.3 on 2023-07-28 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='', verbose_name='companies/logo/')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('region', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('size', models.CharField(max_length=32)),
                ('revenue', models.CharField(max_length=32)),
                ('founded', models.DateField()),
                ('logo', models.ImageField(upload_to='companies/logo/')),
                ('benefits', models.ManyToManyField(related_name='companies', to='company.benefit')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='company.sector')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]