from rest_framework import generics
from company.serialziers import CompanyDetailSerializer, CompanyCreateSerializer, WorkingAtCompanySerializer, \
    CompanyContactSerializer, CompanySectorSerializer, CompanyTechStackSerializer, CompanyListSerializer
from company.models import Company, WorkingAtCompany, Contact, Sector, TechStack


class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CompanyListSerializer
        return CompanyListSerializer


class CompanyCreateView(generics.CreateAPIView):
    queryset = Company.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CompanyCreateSerializer
        return CompanyCreateSerializer


class WorkingCompanyListView(generics.ListAPIView):
    queryset = WorkingAtCompany.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WorkingAtCompanySerializer
        return WorkingAtCompanySerializer


class CompanyContactListView(generics.ListAPIView):
    queryset = Contact.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CompanyContactSerializer
        return CompanyContactSerializer


class CompanySectorListView(generics.ListAPIView):
    queryset = Sector.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.metjod == 'POST':
            return CompanySectorSerializer
        return CompanySectorSerializer


class CompanyTechStackListView(generics.ListAPIView):
    queryset = TechStack.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CompanyTechStackSerializer
        return CompanyTechStackSerializer


class CompanyDetailView(generics.RetrieveAPIView):
    queryset = Company.objects.order_by('-id')
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return CompanyDetailSerializer
        return CompanyDetailSerializer
