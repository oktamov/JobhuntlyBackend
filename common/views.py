from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from common.models import University, Skill
from common.serializers import(
    UniversityDetailSerializers,
    UniversitySerializers,
    UniversityCreateSerializers,
    SkillSerializer
)
from paginations import CustomPageNumberPagination


class UniversityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityDetailSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]


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


class UniversityListView(ListCreateAPIView):
    queryset = University.objects.all()
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UniversityCreateSerializers
        return UniversityCreateSerializers


class SkillListCreateView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
