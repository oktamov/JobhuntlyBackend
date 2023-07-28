from django.contrib import admin

from .models import Company, Benefit, Sector


# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'founded', 'location']
    search_fields = ['name', 'founded']


@admin.register(Benefit)
class BenefitsAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ['name']