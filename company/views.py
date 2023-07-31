from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from company.serialziers import CompanyDetailSerializer, WorkingAtCompanySerializer, \
    CompanyContactSerializer, CompanySectorSerializer, CompanyTechStackSerializer, CompanyListCreateSerializer
from company.models import Company, WorkingAtCompany, Contact, Sector, TechStack
from paginations import CustomPageNumberPagination


class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.order_by('-id')
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    # filterset_fields = ("region", "birth_date")
    ordering_fields = ("name", "size")
    search_fields = ("name", "location")
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CompanyListCreateSerializer
        return CompanyListCreateSerializer


class WorkingCompanyListCreateView(generics.ListCreateAPIView):
    queryset = WorkingAtCompany.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WorkingAtCompanySerializer
        return WorkingAtCompanySerializer


class CompanyContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CompanyContactSerializer
        return CompanyContactSerializer


class CompanySectorLisCreateView(generics.ListCreateAPIView):
    queryset = Sector.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.metjod == 'POST':
            return CompanySectorSerializer
        return CompanySectorSerializer


class CompanyTechStackListCreateView(generics.ListCreateAPIView):
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
