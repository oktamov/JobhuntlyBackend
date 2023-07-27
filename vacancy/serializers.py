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

    def create(self, validated_data):
        user = self.context['request'].user
        if not user.companies.exists():  # Check if user has companies
            raise serializers.ValidationError('User must belong to a company to create a vacancy.')

        company = validated_data.get('company')
        if not user.companies.filter(id=company.id).exists():  # Check if company is in user's companies
            raise serializers.ValidationError('You can only create vacancies for your own company.')

        validated_data['user'] = user
        return super().create(validated_data)
