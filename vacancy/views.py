from rest_framework import generics

from vacancy.custom_permission import IsOwnerOrReadOnly
from vacancy.models import Vacancy
from vacancy.serializers import VacancySerializer


class VacancyListView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class VacancyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    lookup_field = "pk"
    # permission_classes = [IsOwnerOrReadOnly]
