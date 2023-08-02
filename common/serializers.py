from rest_framework import serializers

from common.models import University, Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class UniversitySerializers(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class UniversityCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ("name", "logo")


class UniversityDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ("id", "name", "logo")
        read_only_fields = ("id",)
