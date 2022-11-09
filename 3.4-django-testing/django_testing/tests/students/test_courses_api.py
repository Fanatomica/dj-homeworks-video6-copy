import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user('admin')


@pytest.fixture
def pk():
    return Course.objects.create().id


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_course(client, course_factory):
    # тестирование созданием одного курса через фабрику
    # Arrange
    course = course_factory(_quantity=1)

    # Act
    response = client.get(f'/courses/?id={course[0].id}')
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert len(data) == 1
    assert len(course) == 1
    assert data[0]['name'] == course[0].name


@pytest.mark.django_db
def test_get_course_1(client, pk, course_factory):
    # тестирование через создание экземплчра с помощю фикстуры pk
    # фабрика используется для наполнения базы
    # Arrange
    course_factory(_quantity=20)
    course = Course.objects.all()

    # Act
    response = client.get(f'/courses/?id={pk}')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data[pk-1]['name'] == course[pk-1].name


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    # чтение всех курсов
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.get("/courses/")
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_course_id(client, course_factory):
    # фильтрация по id
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.get(f'/courses/?id={courses[3].id}')
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['id'] == courses[3].id
    assert data[0]['name'] == courses[3].name


@pytest.mark.django_db
def test_filter_course_name(client, course_factory):
    # фильтрация по имени
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.get(f'/courses/?name={courses[5].name}')
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['id'] == courses[5].id
    assert data[0]['name'] == courses[5].name


@pytest.mark.django_db
def test_filter_courses_name(client, course_factory):
    # фильтрация по имени по всему списку
    # Arrange
    courses = course_factory(_quantity=10)

    for i in range(len(courses)):
        # Act
        response = client.get(f'/courses/?name={courses[i].name}')
        data = response.json()

        # Assert
        assert response.status_code == 200
        assert len(data) == 1
        assert data[0]['id'] == courses[i].id
        assert data[0]['name'] == courses[i].name


@pytest.mark.django_db
def test_create_course(client):
    # создание курса
    # Arrange
    data = {"name": "1"}

    # Act
    response = client.post("/courses/", data)
    data1 = response.json()

    # Assert
    assert response.status_code == 201
    assert data1['name'] == '1'


@pytest.mark.django_db
def test_update_course(client, course_factory):
    # изменение курса
    # Arrange
    courses = course_factory(_quantity=10)
    data = {"name": "1"}

    # Act
    response = client.patch('/courses/1/', data)
    data1 = response.json()

    # Assert
    assert response.status_code == 200
    assert data1['name'] == '1'
    assert courses[0].name != '1'


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    # удаление курса
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.delete('/courses/1/')

    # Assert
    assert response.status_code == 204



@pytest.mark.django_db
def test_with_student_max_settings(client, settings, course_factory, student_factory):

    # Arrange
    students = student_factory(_quantity=15)
    courses = course_factory(_quantity=10, students=students)

    # act
    response = client.get(f'/courses/?id={courses[3].id}')
    data = response.json()


    # Assert
    assert response.status_code == 200
    assert len(students) == len(data[0]["students"]) <= settings.MAX_STUDENTS_PER_COURSE






