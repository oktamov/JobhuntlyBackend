from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from company.serialziers import CompanyDetailSerializer, WorkingAtCompanySerializer, \
    CompanyContactSerializer, CompanySectorSerializer, CompanyTechStackSerializer, CompanyListCreateSerializer
from company.models import Company, WorkingAtCompany, Contact, Sector, TechStack
from paginations import CustomPageNumberPagination
from vacancy.custom_permission import IsOwnerOrReadOnly


class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.order_by('-id')
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('sector__name', 'size')
    ordering_fields = ('id', 'created_at')
    search_fields = ("name", "location")
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CompanyListCreateSerializer
        return CompanyListCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkingCompanyCreateView(generics.CreateAPIView):
    queryset = WorkingAtCompany.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WorkingAtCompanySerializer
        return WorkingAtCompanySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkingCompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkingAtCompany.objects.order_by('-id')
    lookup_field = "pk"
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = WorkingAtCompanySerializer


class CompanyContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CompanyContactSerializer
        return CompanyContactSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CompanyContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.order_by('-id')
    lookup_field = "pk"
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CompanyContactSerializer


class CompanySectorCreateView(generics.CreateAPIView):
    queryset = Sector.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CompanySectorSerializer
        return CompanySectorSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CompanySectorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sector.objects.order_by('-id')
    lookup_field = "pk"
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CompanySectorSerializer


class CompanyTechStackCreateView(generics.CreateAPIView):
    queryset = TechStack.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CompanyTechStackSerializer
        return CompanyTechStackSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CompanyTechStackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TechStack.objects.order_by('-id')
    lookup_field = "pk"
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CompanyTechStackSerializer


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.order_by('-id')
    lookup_field = "pk"
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CompanyDetailSerializer
