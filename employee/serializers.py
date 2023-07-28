from rest_framework import serializers

from .models import Employee, Experience, Skill, EmployeeSkill, Education, University


class EmployeeListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("user", "region", "birth_date", "gender")


class EmployeeDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Employee
        fields = ("id", "user", "region", "birth_date", "gender")


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


# class EmployeeExperienceSkillSerializer(serializers.ModelSerializer):
#     experiences = ExperienceSerializer(many=True)
#     skills = EmployeeSkillSerializer(source='employeeskills', many=True)
#
#     class Meta:
#         model = Employee
#         fields = ("id", "student_to", " student_from", "gpa")


class EducationListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ("student_to", "student_from", "gpa")


class EducationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ("id", "student_to", "student_from", "gpa")
        read_only_fields = ("id",)


class EducationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Education
        fields = ("id", "student_to", "student_from", "gpa")


class UniversitySerializers(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class UniversityCreateSerializers(serializers.ModelSerializer):
    class Mate:
        model = University
        fields = ("name", "logo")


class UniversityDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ("id", "name", "logo")
        read_only_fields = ("id",)
