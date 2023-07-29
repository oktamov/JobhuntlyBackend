import pytest
from model_bakery import baker
from django.db.utils import IntegrityError
from employee.models import Employee, Experience, Education, University, Skill, EmployeeSkill


@pytest.mark.django_db
def test_employee_creation():
    employee = baker.make(Employee)
    assert Employee.objects.count() == 1
    assert str(employee) == employee.user.get_full_name()


@pytest.mark.django_db
def test_experience_creation():
    employee = baker.make(Employee)
    company = baker.make('company.Company')

    experience = baker.make(Experience, employee=employee, company=company)
    assert Experience.objects.count() == 1


@pytest.mark.django_db
def test_education_creation():
    employee = baker.make(Employee)
    university = baker.make(University)

    education = baker.make(Education, employee_id=employee, university_id=university)
    assert Education.objects.count() == 1


@pytest.mark.django_db
def test_skill_creation():
    skill = baker.make(Skill)
    assert Skill.objects.count() == 1


@pytest.mark.django_db
def test_employee_skill_creation():
    employee = baker.make(Employee)
    skill = baker.make(Skill)

    employee_skill = baker.make(EmployeeSkill, employee=employee, skill=skill)
    assert EmployeeSkill.objects.count() == 1

    with pytest.raises(IntegrityError):
        baker.make(EmployeeSkill, employee=employee, skill=skill)
