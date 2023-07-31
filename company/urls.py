from django.urls import path
from company.views import CompanyListCreateView, CompanyDetailView, CompanyContactListView, \
    CompanyTechStackListView, CompanySectorListView, WorkingCompanyListView

urlpatterns = [
    path('list-create/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('contact/', CompanyContactListView.as_view(), name='company-contact'),
    path('tech-stack/', CompanyTechStackListView.as_view(), name='company-tech-stack'),
    path('sector/', CompanySectorListView.as_view(), name='company-sector'),
    path('working/', WorkingCompanyListView.as_view(), name='company-working'),

]
