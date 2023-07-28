import pytest
from django.urls import reverse
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def new_vacancy():
    return baker.make("vacancy.Vacancy")


@pytest.fixture
def new_company():
    return baker.make("company.Company")


@pytest.fixture
def new_user():
    return baker.make("users.User")


@pytest.mark.django_db
class TestVacancy:
    def test_vacancy_list(self, client):
        url = reverse("list")
        response = client.get(url)
        assert response.status_code == 200

    def test_vacancy_detail(self, client, new_vacancy):
        url = reverse("detail", kwargs={"pk": new_vacancy.pk})
        response = client.get(url)
        assert response.status_code == 200

    def test_vacancy_create(self, new_vacancy, new_user, new_company):
        url = reverse("create")
        client = APIClient()
        client.force_authenticate(user=new_user)
        data = {"title": "new",
                "experience": "experience",
                "level": "Junior",
                "job_type": "full time",
                "salary": 0,
                "company": new_company.id,
                "user": new_user.id
                }
        response = client.post(url, data)
        assert response.status_code == 400

    def test_vacancy_applycations(self,client, new_vacancy):
        url = reverse("application-list", kwargs={"pk": new_vacancy.pk})
        response = client.get(url)
        assert response.status_code == 200

