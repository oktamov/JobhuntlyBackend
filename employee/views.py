from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from common.serializers import UniversityDetailSerializers
from employee.serializers import (
    ExperienceSerializer,
    EmployeeSkillSerializer,
    EmployeeListCreateSerializer,
    EmployeeDetailSerializer,
    EducationSerializer,
    EducationDetailSerializer,
    EducationListCreateSerializer, UniversitySerializers,
)
from paginations import CustomPageNumberPagination
from .models import Employee, Experience, EmployeeSkill, Education, University
from .permissions import IsOwnerOrReadOnly


class EmployeeListView(ListCreateAPIView):
    queryset = Employee.objects.all()
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return EmployeeListCreateSerializer
        return EmployeeListCreateSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.order_by("-id")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ("region", "birth_date")
    ordering_fields = ("id", "username")
    search_fields = ("username", "gender")
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return EmployeeDetailSerializer
        return EmployeeDetailSerializer


class EmployeeSkillListCreateView(generics.ListCreateAPIView):
    queryset = EmployeeSkill.objects.all()
    serializer_class = EmployeeSkillSerializer
    permission_classes = [IsAuthenticated]


class ExperienceListCreateView(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class EmployeeSkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeSkill.objects.all()
    serializer_class = EmployeeSkillSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]


class EducationListCreateView(generics.ListCreateAPIView):
    queryset = Education.objects.order_by("-id")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    search_fields = ("student_to", "student_from", "gpa")
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = EducationSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return EducationDetailSerializer
        return EducationDetailSerializer


class EducationListView(ListCreateAPIView):
    queryset = Education.objects.all()
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return EducationListCreateSerializer
        return EducationListCreateSerializer


class UniversityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityDetailSerializers
    permission_classes = [IsOwnerOrReadOnly]


class UniversityListCreateView(generics.ListCreateAPIView):
    queryset = University.objects.order_by("-id")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    search_fields = ("name", "logo")
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UniversitySerializers

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UniversityDetailSerializers
        return UniversityDetailSerializers
