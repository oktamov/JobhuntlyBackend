from django_filters import rest_framework as filters

from vacancy.models import Vacancy


class VacancyFilters(filters.FilterSet):
    min_salary = filters.NumberFilter(field_name='salary', lookup_expr='gte')
    max_salary = filters.NumberFilter(field_name='salary', lookup_expr='lte')
    job_type = filters.CharFilter(field_name='job_type', lookup_expr='icontains')
    level = filters.CharFilter(field_name='level', lookup_expr='icontains')

    class Meta:
        model = Vacancy
        fields = ['min_salary', 'max_salary', 'job_type', 'level']
