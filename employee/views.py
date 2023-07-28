from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from paginations import CustomPageNumberPagination
from employee.serializers import (
    EmployeeExperienceSkillSerializer,
    ExperienceSerializer,
    SkillSerializer,
    EmployeeSkillSerializer,
    EmployeeListCreateSerializer,
    EmployeeDetailSerializer,
)

from .models import Employee, Experience, Skill, EmployeeSkill


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


class SkillListCreateView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class EmployeeSkillListCreateView(generics.ListCreateAPIView):
    queryset = EmployeeSkill.objects.all()
    serializer_class = EmployeeSkillSerializer
    permission_classes = [IsAuthenticated]


class ExperienceListCreateView(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class EmployeeExperienceSkillListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeExperienceSkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class EmployeeSkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeSkill.objects.all()
    serializer_class = EmployeeSkillSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

