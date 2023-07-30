from django.urls import path
from company.views import CompanyListCreateView, CompanyDetailView

urlpatterns = [
    path('', CompanyListCreateView.as_view(), name='company-lisr-create'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
]
