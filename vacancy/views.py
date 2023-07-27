from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from paginations import CustomPageNumberPagination
from vacancy.custom_permission import IsOwnerOrReadOnly
from vacancy.filters import VacancyFilters
from vacancy.models import Vacancy
from vacancy.serializers import VacancySerializer


class VacancyListView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = VacancyFilters
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
