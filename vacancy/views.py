from rest_framework import generics, permissions, serializers
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from paginations import CustomPageNumberPagination
from vacancy.custom_permission import IsOwnerOrReadOnly
from vacancy.models import Vacancy, Application
from vacancy.serializers import VacancySerializer, ApplicationSerializer, ApplicationListSerializer


class VacancyListView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = ("salary", 'updated_year')
    search_fields = ("title", "job_type", "experience", "level")
    pagination_class = CustomPageNumberPagination


class VacancyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    lookup_field = "pk"
    permission_classes = [IsOwnerOrReadOnly]


class VacancyCreateView(generics.CreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        vacancy_id = self.kwargs.get('vacancy_id')  # Get vacancy ID from URL
        vacancy = Vacancy.objects.filter(id=vacancy_id).first()
        if not vacancy:
            raise serializers.ValidationError('A vacancy with this ID does not exist.')
        serializer.save(vacancy=vacancy)


class ApplicationListView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationListSerializer
    lookup_field = 'pk'
