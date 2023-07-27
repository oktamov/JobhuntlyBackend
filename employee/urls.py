from django.urls import path

from employee.views import (
    EmployeeListCreateView,
    EmployeeListView,
    EmployeeDetailView
)


app_name = "employee"

urlpatterns = [
    path("", EmployeeListCreateView.as_view(), name="employee_list_create"),
    path("", EmployeeListView.as_view(), name="employee_list"),
    path("<int:pk>/", EmployeeDetailView.as_view(), name="employee_detail")
]
