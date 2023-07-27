from rest_framework import serializers

from vacancy.models import Vacancy


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = (
            'id', 'title', 'experience', 'level', 'job_type', 'salary', 'overview', 'description', 'offer',
            'created_at', 'user')
