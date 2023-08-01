from django.urls import path
from company.views import CompanyListCreateView, CompanyDetailView, CompanyContactListCreateView, \
    CompanyTechStackListCreateView, CompanySectorLisCreateView, WorkingCompanyListCreateView

urlpatterns = [
    path('list-create/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('contact/', CompanyContactListCreateView.as_view(), name='company-contact'),
    path('tech-stack/', CompanyTechStackListCreateView.as_view(), name='company-tech-stack'),
    path('sector/', CompanySectorLisCreateView.as_view(), name='company-sector'),
    path('working/', WorkingCompanyListCreateView.as_view(), name='company-working'),

]
