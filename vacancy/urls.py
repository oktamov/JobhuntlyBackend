from django.urls import path

from vacancy.views import VacancyListView, VacancyDetailView

urlpatterns = [
    path('', VacancyListView.as_view(), name='list'),
    path('<int:pk>', VacancyDetailView.as_view(), name='detail'),
]
