from django.urls import path
from company.views import CompanyListCreateView, CompanyDetailView, CompanyContactCreateView, \
    CompanyTechStackCreateView, CompanySectorCreateView, WorkingCompanyCreateView, CompanyContactDetailView, \
    CompanySectorDetailView, CompanyTechStackDetailView, WorkingCompanyDetailView

urlpatterns = [
    path('list-create/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('contact/', CompanyContactCreateView.as_view(), name='company-contact'),
    path('contact/<int:pk>/', CompanyContactDetailView.as_view(), name='company-contact-detail'),
    path('tech-stack/', CompanyTechStackCreateView.as_view(), name='company-tech-stack'),
    path('tech-stack/<int:pk>/', CompanyTechStackDetailView.as_view(), name='company-tech-stack-detail'),
    path('sector/', CompanySectorCreateView.as_view(), name='company-sector'),
    path('sector/<int:pk>/', CompanySectorDetailView.as_view(), name='company-sector-detail'),
    path('working/', WorkingCompanyCreateView.as_view(), name='company-working'),
    path('working/<int:pk>/', WorkingCompanyDetailView.as_view(), name='company-working-detail'),

]
