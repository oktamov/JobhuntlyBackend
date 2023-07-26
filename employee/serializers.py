from rest_framework import serializers

from employee.models import Employee


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
        fields = ("id", "username", "region", "birth_date", "gender")
