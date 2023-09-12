from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from education.models import Course, Lesson
from users.models import User, UserRoles

class LessonTestCase(APITestCase):

    def setUp(self):
        """Заполнение первичных данных"""

        self.user = User.objects.create(
            email='test@test.ru',
            is_staff=True,
            is_superuser=True,
            is_active=True,
            role=UserRoles.MEMBER,
        )
        self.user.set_password('324214Kross!')
        self.user.save()

        token = RefreshToken.for_user(self.user)
        self.access_token = str(token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.course = Course.objects.create(
            title='course test',
            description='course test'
        )

        self.lesson = Lesson.objects.create(
            title='lesson test',
            description='lesson test',
            course=self.course,
            author=self.user
        )

    def test_lesson_list(self):
        """ Тест получения списка уроков"""

        response = self.client.get(
            reverse('education:lesson_list'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # print(response.json())

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': self.lesson.id, 'title': 'lesson test', 'description': 'lesson test', 'preview': None,
                 'link': None,
                 'course': self.course.id, 'author': self.user.id}]}
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_create_lesson(self):
        """ Тест создания уроков"""

        data = {
            'title': 'test create',
            'description': 'test create'
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            reverse('education:lesson_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )
    def test_lesson_update(self):
        """ Тест обновления урока """
        self.client.force_authenticate(user=self.user)

        data = {
            'title': 'update lesson',
            'description': 'update lesson',
        }

        response = self.client.put(
            path=f'/lesson/update/{self.lesson.id}/',
            data=data,
        )

        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )
        response = response.json()

        self.assertTrue(
            Lesson.objects.all().exists()
        )
    def test_lesson_delete(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            f'/lesson/delete/{self.lesson.id}/',
        )

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT,
        )
        self.assertFalse(
            Lesson.objects.all().exists(),
        )

    def tearDown(self) -> None:
        self.user.delete()
        self.course.delete()
        self.lesson.delete()


class SubscriptionTest(APITestCase):
    def setUp(self) -> None:
        """Заполнение первичных данных"""
        self.course = Course.objects.create(
            title='test_course',
            description='test_course'
        )

        self.user = User.objects.create(
            email='test@test.com',
            is_staff=False,
            is_superuser=True,
            is_active=True,
            role=UserRoles.MEMBER,
        )
        self.user.set_password('324214Kross!')
        self.user.save()

        token = RefreshToken.for_user(self.user)
        self.access_token = str(token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_subscription(self):
        response = self.client.post('/subscription/create/',
                                    {'course': self.course.id, 'user': self.user.id, 'status': False})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)