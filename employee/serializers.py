from rest_framework import serializers

from employee.models import Employee, Education


class EmployeeListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("username", "region", "birth_date", "gender")


class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "username", "region", "birth_date", "gender")
        read_only_fields = ("id",)


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Employee
        fields = ("id", "student_to", " student_from", "gpa")


class EducationListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ("student_to", " student_from", "gpa")


class EducationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ("id", "student_to", " student_from", "gpa")
        read_only_fields = ("id",)


class EducationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Education
        fields = ("id", "student_to", " student_from", "gpa")
