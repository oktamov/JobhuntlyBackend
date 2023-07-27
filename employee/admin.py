from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'region', 'birth_date', 'gender']
    # ordering = ['-created_at']
