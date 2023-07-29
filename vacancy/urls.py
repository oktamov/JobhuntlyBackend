from django.urls import path

from vacancy.views import VacancyListView, VacancyDetailView, VacancyCreateView, ApplicationCreateView, \
    ApplicationListView

urlpatterns = [
    path('', VacancyListView.as_view(), name='list'),
    path('<int:pk>', VacancyDetailView.as_view(), name='detail'),
    path('create/', VacancyCreateView.as_view(), name='create'),
    path('<int:id>/application/create/', ApplicationCreateView.as_view(), name='application-create'),
    path('<int:pk>/application/list', ApplicationListView.as_view(), name='application-list'),
]
