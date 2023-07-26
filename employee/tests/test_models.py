import pytest
from model_bakery import baker


@pytest.mark.django_db
def test_student_str():
    username = "Test employee"
    employee = baker.make("employee.Employee", full_name=username)
    assert str(employee) == employee
