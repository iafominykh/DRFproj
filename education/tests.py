from rest_framework import status
from rest_framework.test import APITestCase
from education.models import Course
from users.models import User, UserRoles


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        """заполнение первичных данных"""
        self.user = User.objects.create(
            email='test@test.com',
            is_staff=False,
            is_superuser=False,
            is_active=True,
            role=UserRoles.MEMBER,
        )
        self.user.set_password('Aa123123')
        self.user.save()
        response = self.client.post('/users/api/token/', {"email": "test@test.com", "password": "Aa123123"})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_lesson(self):
        """Тестирование создания урока"""
        response = self.client.post('/lesson/create/',
                                    {'title': 'lesson 1', 'description': 'lesson a/an', 'author': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response2 = self.client.post('/lesson/create/',
                                     {'title': 'lesson 2', 'description': 'lesson 2', 'link': 'www.youtube.com'})
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_lesson(self):
        """Тестирование вывода списка уроков"""
        self.test_create_lesson()
        response = self.client.get('/lesson/')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'count': 1, 'next': None, 'previous': None, 'results': [
            {'id': 1, 'title': 'lesson 1', 'description': 'lesson a/an', 'preview': None,
             'link': None, 'course': None, 'author': 1}]})

    def test_retrieve_lesson(self):
        self.test_create_lesson()
        response = self.client.get('/lesson/detail/1/')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'id': 1, 'title': 'lesson 1', 'description': 'lesson a/an', 'preview': None,
                                           'link': None, 'course': None, 'author': 1})


class SubscriptionTest(APITestCase):
    def setUp(self) -> None:
        """заполнение первичных данных"""
        self.course = Course.objects.create(
            title='test_course',
            description='test_course'
        )

        self.user = User.objects.create(
            email='test@test.com',
            city='Moscow',
            is_staff=False,
            is_superuser=True,
            is_active=True,
            role=UserRoles.MEMBER,
        )
        self.user.set_password('Aa123123')
        self.user.save()
        response = self.client.post('/users/api/token/', {"email": "test@test.com", "password": "Aa123123"})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_subscription(self):
        response = self.client.post('/subscription/create/',
                                    {'course': self.course.id, 'user': self.user.id, 'status': False})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)