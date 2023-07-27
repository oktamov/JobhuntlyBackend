from rest_framework import generics, permissions

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
    permission_classes = [IsOwnerOrReadOnly]


class VacancyCreateView(generics.CreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create a vacancy

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




