from django.urls import path

from employee.views import (
    EmployeeListCreateView,
    EmployeeListView,
    EmployeeDetailView,
    EmployeeSkillListCreateView,
    EmployeeSkillDetailView,
    ExperienceListCreateView,
    ExperienceDetailView,
    EducationDetailView,
    EducationListCreateView,
    EducationListView,
    UniversityListCreateView,
    UniversityDetailView
)

app_name = "employee"

urlpatterns = [
    path("", EmployeeListCreateView.as_view(), name="employee_list_create"),
    path("", EmployeeListView.as_view(), name="employee_list"),
    path("<int:pk>/", EmployeeDetailView.as_view(), name="employee_detail"),
    path('skills/', EmployeeSkillListCreateView.as_view(), name='employee-skill-list-create'),
    path('skills/<int:pk>/', EmployeeSkillDetailView.as_view(), name='employee-skill-detail'),
    path('experiences/', ExperienceListCreateView.as_view(), name='experience-list-create'),
    path('experiences/<int:pk>/', ExperienceDetailView.as_view(), name='experience-detail'),
    path('education/<int:pk>/', EducationDetailView.as_view(), name="education-detail"),
    path('education-list-create/', EducationListCreateView.as_view(), name="education-list-create"),
    path('education-list/', EducationListView.as_view(), name="education-list"),
    path('university/<int:pk>/', UniversityDetailView.as_view(), name="university-detail"),
    path('university-list-create/', UniversityListCreateView.as_view(), name="university-list-create"),

]
