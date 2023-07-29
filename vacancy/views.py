from rest_framework import generics, permissions, serializers, status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from employee.models import Employee
from paginations import CustomPageNumberPagination
from vacancy.custom_permission import IsOwnerOrReadOnly
from vacancy.filters import VacancyFilters
from vacancy.models import Vacancy, Application
from vacancy.serializers import VacancySerializer, ApplicationSerializer, ApplicationListSerializer, \
    VacancyListSerializer


class VacancyListView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = ("salary", 'updated_year')
    search_fields = ("title", "job_type", "experience", "level")
    filterset_class = VacancyFilters
    pagination_class = CustomPageNumberPagination


class VacancyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer
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
        vacancy_id = self.kwargs.get('id')  # Get vacancy ID from URL
        vacancy = Vacancy.objects.get(id=vacancy_id)
        employee = Employee.objects.get(user=self.request.user)
        if not vacancy:
            raise serializers.ValidationError('A vacancy with this ID does not exist.')
        try:
            Application.objects.get(vacancy=vacancy, employee=employee)
            raise serializers.ValidationError("You have already applied for this vacancy")
        except Application.DoesNotExist:
            application = Application(vacancy=vacancy, employee=employee)
            application.save()
            return Response({"detail": "successfully added"}, status=status.HTTP_201_CREATED)


class ApplicationListView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationListSerializer
    lookup_field = 'pk'
