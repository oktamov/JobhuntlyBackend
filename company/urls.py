from django.urls import path
from company.views import CompanyListView, CompanyCreateView, CompanyDetailView, CompanyContactListView, \
    CompanyTechStackListView, \
    CompanySectorListView, WorkingCompanyListView

urlpatterns = [
    path('', CompanyListView.as_view(), name='company-lisr'),
    path('', CompanyCreateView.as_view(), name='company-lisr'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('contact/', CompanyContactListView.as_view(), name='company-contact'),
    path('tech-stack/', CompanyTechStackListView.as_view(), name='company-tech-stack'),
    path('sector/', CompanySectorListView.as_view(), name='company-sector'),
    path('working/', WorkingCompanyListView.as_view(), name='company-working'),

]
