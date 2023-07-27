from rest_framework import serializers

from employee.models import Employee
from users.serializers import UserSerializer
from vacancy.models import Vacancy, Application


class VacancySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Vacancy
        fields = (
            'id', 'title', 'experience', 'level', 'job_type', 'salary', 'overview', 'description', 'offer',
            'num_applications',
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


class Application1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'created_at')

    def create(self, validated_data):
        user = self.context['request'].user
        vacancy = self.context['request'].vacancy
        if not user.employees.exists():
            raise serializers.ValidationError('First create an employee')
        employee = user.employees
        if not user.employees.filter(id=employee.id).exists():
            raise serializers.ValidationError('You can only submit a vacancy for your own employee')

        validated_data['employees'] = employee
        validated_data['vacancy'] = vacancy
        return super().create(validated_data)


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'created_at')

    def create(self, validated_data):
        user = self.context['request'].user
        employee = Employee.objects.filter(user=user).first()
        if not employee:
            raise serializers.ValidationError('The user must have an associated employee to create an application.')

        vacancy = self.context['view'].kwargs.get('vacancy_id')
        if Application.objects.filter(employee=employee, vacancy=vacancy).exists():
            raise serializers.ValidationError('This employee has already applied for this vacancy.')

        validated_data['employee'] = employee
        return super().create(validated_data)
