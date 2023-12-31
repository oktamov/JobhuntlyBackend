from django.contrib import admin

from .models import User


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name']
