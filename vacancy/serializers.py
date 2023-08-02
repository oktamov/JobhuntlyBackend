from rest_framework import serializers

from employee.models import Employee, Skill
from users.serializers import UserSerializer
from vacancy.models import Vacancy, Application


class VacancySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Vacancy
        fields = (
            'id', 'title', 'experience', 'level', 'job_type', 'salary', 'overview', 'description', 'offer',
            'created_at', 'user', 'company', 'skills')

    def create(self, validated_data):
        user = self.context['request'].user
        if not user.companies.exists():
            raise serializers.ValidationError('User must belong to a company to create a vacancy.')

        company = validated_data.get('company')
        if not user.companies.filter(id=company.id).exists():
            raise serializers.ValidationError('You can only create vacancies for your own company.')

        validated_data['user'] = user
        return super().create(validated_data)


class VacancyPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = (
            'id', 'title', 'experience', 'level', 'job_type', 'salary', 'overview', 'description', 'offer',
            'user', 'company', 'skills')


class SkillForVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name',)


class VacancyListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    skills = SkillForVacancySerializer(many=True)

    class Meta:
        model = Vacancy
        fields = (
            'id', 'title', 'experience', 'level', 'job_type', 'salary', 'overview', 'description', 'offer',
            'num_applications',
            'created_at', 'company', 'user', 'skills')


class ApplicationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'employee', 'vacancy', 'created_at')


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'created_at')
