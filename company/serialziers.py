from rest_framework import serializers

from company.models import Company, Benefit, Sector, TechStack, Contact, WorkingAtCompany


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'description', 'logo', 'sector')


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'description', 'logo', 'sector')


class CompanySectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ('name',)


class CompanyTechStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechStack
        fields = ('logo', 'name')


class CompanyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('company', 'url', 'contact')


class WorkingAtCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingAtCompany
        fields = ('company', 'image')


class CompanyBenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = ('name', 'description', 'logo')


class CompanyDetailSerializer(serializers.ModelSerializer):
    benefits = CompanyBenefitsSerializer(many=True)
    sector = CompanySectorSerializer()
    tech_stack = CompanyTechStackSerializer(many=True)
    contact = CompanyContactSerializer(many=True)
    working_company = WorkingAtCompanySerializer(many=True)

    class Meta:
        model = Company
        fields = (
            'name', 'description', 'logo', 'founded', 'benefits', 'sector', 'tech_stack', 'contact', 'working_company')
