from rest_framework import serializers
from .models import Employee, Experience, Skill, EmployeeSkill


class EmployeeListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("username", "region", "birth_date", "gender")


class EmployeeDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Employee
        fields = ("id", "username", "region", "birth_date", "gender")


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class EmployeeSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()

    class Meta:
        model = EmployeeSkill
        fields = ('skill',)


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class EmployeeExperienceSkillSerializer(serializers.ModelSerializer):
    experiences = ExperienceSerializer(many=True)
    skills = EmployeeSkillSerializer(source='employeeskills', many=True)

    class Meta:
        model = Employee
        fields = '__all__'
