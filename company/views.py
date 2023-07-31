from rest_framework import generics
from rest_framework.views import APIView

from company.serialziers import CompanyDetailSerializer, CompanyCreateSerializer
from company.models import Company


class CompanyListCreateView(generics.ListAPIView):
    queryset = Company.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CompanyCreateSerializer
        return CompanyCreateSerializer


class CompanyDetailView(generics.RetrieveAPIView):
    queryset = Company.objects.order_by('-id')
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return CompanyDetailSerializer
        return CompanyDetailSerializer
