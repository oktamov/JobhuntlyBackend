from rest_framework import serializers
from company.models import Company, Benefit, Sector, TechStack, Contact, WorkingAtCompany
from users.serializers import UserSerializer


class CompanyListCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Company
        fields = (
            'id', 'user', 'name', 'region', 'location', 'description', 'size', 'revenue', 'founded', 'logo', 'sector',
            'benefits', 'tech_stacks', 'job_count', 'created_at')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)


class CompanySectorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Sector
        fields = ('id', 'name', 'user')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)


class CompanyTechStackSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TechStack
        fields = ('id', 'logo', 'name', 'user')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)


class CompanyContactSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Contact
        fields = ('id', 'company', 'url', 'contact', 'user')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)


class WorkingAtCompanySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    image = serializers.ImageField

    class Meta:
        model = WorkingAtCompany
        fields = ('id', 'company', 'image', 'user')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)


class CompanyBenefitsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Benefit
        fields = ('id', 'name', 'description', 'logo', 'user')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)


class CompanyDetailSerializer(serializers.ModelSerializer):
    benefits = CompanyBenefitsSerializer(many=True)
    sector = CompanySectorSerializer()
    tech_stacks = CompanyTechStackSerializer(many=True)
    contacts = CompanyContactSerializer(many=True)
    images = WorkingAtCompanySerializer(many=True)

    class Meta:
        model = Company
        fields = (
            'id', 'name', 'description', 'logo', 'founded', 'benefits', 'sector', 'tech_stacks', 'contacts',
            'images', 'user')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
