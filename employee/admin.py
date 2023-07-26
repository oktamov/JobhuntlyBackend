from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'region', 'birth_date', 'gender']
    ordering = ['-date_joined']
