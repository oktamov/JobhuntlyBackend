import pytest
from model_bakery import baker
from django.db.utils import IntegrityError
from employee.models import Employee, Experience, Education, Skill, EmployeeSkill
from common.models import University


@pytest.mark.django_db
def test_employee_creation():
    employee = baker.make(Employee)
    assert Employee.objects.count() == 1
    assert str(employee) == employee.user.email


@pytest.mark.django_db
def test_experience_creation():
    employee = baker.make(Employee)
    company = baker.make('company.Company')

    experience = baker.make(Experience, employee=employee, company=company)
    assert Experience.objects.count() == 1


@pytest.mark.django_db
def test_education_model():
    employee = baker.make('employee.Employee')
    university = baker.make('common.University')
    education = baker.make('employee.Education', employee=employee, university=university)

    db_education = Education.objects.get(pk=education.pk)

    assert db_education.student_to == education.student_to
    assert db_education.student_from == education.student_from
    assert db_education.gpa == education.gpa
    assert db_education.employee == employee
    assert db_education.university == university

    gpa_value = 3
    education_with_specific_values = baker.make('employee.Education', employee=employee, university=university, gpa=gpa_value)
    assert education_with_specific_values.gpa == gpa_value

    assert employee.education.first() == education
    assert university.education.first() == education


@pytest.mark.django_db
def test_skill_creation():
    skill = baker.make(Skill)
    assert Skill.objects.count() == 1


@pytest.mark.django_db
def test_employee_skill_creation():
    employee = baker.make(Employee)
    skill = baker.make(Skill)

    employee_skill = baker.make(EmployeeSkill, employee=employee, skill=skill)

    assert isinstance(employee_skill, EmployeeSkill)
    assert employee_skill.employee == employee
    assert employee_skill.skill == skill

    expected_str = f"{employee} - {skill}"
    assert str(employee_skill) == expected_str

    with pytest.raises(Exception):
        baker.make(EmployeeSkill, employee=employee, skill=skill)
