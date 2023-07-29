from django.contrib import admin

from .models import Company, Benefit, Sector, Contact, TechStack, WorkingAtCompany


# Register your models here.
@admin.register(WorkingAtCompany)
class WorkingAtCompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['url', 'company_name']

    def company_name(self, obj):
        return obj.company.name


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
