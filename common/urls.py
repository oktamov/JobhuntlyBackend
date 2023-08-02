from django.urls import path

from common.views import (
    UniversityDetailView,
    UniversityListCreateView,
    UniversityListView,
    SkillListCreateView,
    SkillDetailView
)

app_name = "common"

urlpatterns = [
    path('university/<int:pk>/', UniversityDetailView.as_view(), name="university-detail"),
    path('university-list-create/', UniversityListCreateView.as_view(), name="university-list-create"),
    path('university-list/', UniversityListView.as_view(), name="university-list"),
    path('skills/', SkillListCreateView.as_view(), name='skill-list-create'),
    path('skills/<int:pk>/', SkillDetailView.as_view(), name='skill-detail')
]
