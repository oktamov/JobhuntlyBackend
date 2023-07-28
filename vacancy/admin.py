from django.contrib import admin

from vacancy.models import Vacancy, Application


@admin.register(Vacancy)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['title', 'experience']


admin.site.register(Application)

