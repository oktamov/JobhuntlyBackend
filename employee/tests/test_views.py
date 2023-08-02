import pytest
from model_bakery import baker
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from employee.models import Employee, Education
from employee.views import EmployeeListView


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_employee_list_view():
    baker.make(Employee, _quantity=5)
    factory = APIRequestFactory()
    request = factory.get('/api/employees/')
    view = EmployeeListView.as_view()
    response = view(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_employee_list(api_client):
    baker.make(Employee, _quantity=5)

    url = reverse("employee:employee_list")
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 5


@pytest.mark.django_db
def test_employee_create():
    client = APIClient()
    baker.make(Employee, _quantity=5)
    response = client.get(reverse('employee:employee_list'))

    assert response.status_code == 200
    assert len(response.data) == 5

    data = {'name': 'Test Employee'}
    response = client.post(reverse('employee:employee_list'), data)

    assert response.status_code == 403


# @pytest.mark.django_db
# class TestEducationListCreateView:
#     @pytest.fixture
#     def api_client(self):
#         return APIClient()
#
#     @pytest.fixture
#     def sample_education_data(self):
#         return {
#             "student_to": "John Doe",
#             "student_from": "Jane Smith",
#             "gpa": 3.7,
#         }
#
#     def test_create_education(self, api_client, sample_education_data):
#         url = reverse("employee:education-list-create")
#         response = api_client.post(url, data=sample_education_data)
#
#         assert response.status_code == status.HTTP_403_FORBIDDEN  # HTTP_201_CREATED
#         assert Education.objects.count() == 0  # 1


@pytest.mark.django_db
def test_education_list_create():
    client = APIClient()
    baker.make(Education, _quantity=5)
    response = client.get(reverse('employee:employee_list'))

    assert response.status_code == 200
    assert len(response.data) == 5

    data = {'name': 'Test Employee'}
    response = client.post(reverse('employee:employee_list'), data)

    assert response.status_code == 403


@pytest.mark.django_db
def test_list_education(api_client):
    baker.make(Education, _quantity=3)
    url = reverse("employee:education-list-create")
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 5


@pytest.mark.django_db
def test_education_list_create_api_view():
    client = APIClient()
    baker.make(Education, _quantity=5)
    response = client.get(reverse('employee:education-list'))

    assert response.status_code == 200
    assert len(response.data) == 5

    data = {'name': 'Test Education'}
    response = client.post(reverse('employee:education-list'), data)

    assert response.status_code == 400
