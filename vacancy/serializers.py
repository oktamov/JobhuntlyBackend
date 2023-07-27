from rest_framework import serializers

from users.serializers import UserSerializer
from vacancy.models import Vacancy


class VacancySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Vacancy
        fields = (
            'id', 'title', 'experience', 'level', 'job_type', 'salary', 'overview', 'description', 'offer',
            'created_at', 'company', 'user')
