from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView
from paginations import CustomPageNumberPagination
from employee.serializers import (
    EmployeeListCreateSerializer,
    EmployeeSerializer,
    EmployeeDetailSerializer
)

from .models import Employee


class EmployeeListView(ListCreateAPIView):
    queryset = Employee.objects.all()
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return EmployeeListCreateSerializer
        return EmployeeListCreateSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.request.method in ["POST", "PATCH"]:
            return EmployeeDetailSerializer
        return EmployeeDetailSerializer


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.order_by("-id")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ("region", "birth_date")
    ordering_fields = ("id", "username")
    search_fields = ("username", "gender")
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return EmployeeSerializer
        return EmployeeSerializer
