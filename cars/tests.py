from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from .models import User, Car
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()


class AuthTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('username_test', 'test@mail.ru', 'password')
        self.user.is_staff = False
        self.user.is_superuser = False
        self.user.is_active = True
        self.user.save()

    def testLogin(self):
        self.client.login(userncleame='test@mail.ru', password='password')


class CarAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(username="username_test", email="test@mail.ru")
        self.user.set_password("password")
        self.token = Token.objects.create(user=self.user)
        self.car = Car.objects.create(name="Ваз 2106 ", created_date="1976-01-01", added_date=date.today())
        self.user.save()

    def test_create_user(self):
        self.client.force_login(user=self.user)
        url = '/api/users/'
        data = {"username": "test_user", "email": "test_user@mail.ru", "password": "123456", "cars":[]}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(url, data, format('json'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 2)

    def test_create_car(self):
        self.client.force_login(user=self.user)
        url = '/api/cars/'
        data = {"name": "Ваз 2016", "created_date": "1976-01-01", "added_date": date.today()}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(url, data, format('json'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Car.objects.count(), 2)

    def test_get_users_list(self):
        self.client.force_login(user=self.user)
        url = '/api/users/'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {}
        response = self.client.get(url, data, format('json'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_cars_list(self):
        self.client.force_login(user=self.user)
        url = '/api/cars/'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {}
        response = self.client.get(url, data, format('json'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_detail(self):
        self.client.force_login(user=self.user)
        url = '/api/users/'+str(self.user.id)+"/"
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {}
        response = self.client.get(url, data, format('json'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_car_detail(self):
        self.client.force_login(user=self.user)
        url = '/api/cars/'+str(self.car.id)+"/"
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {}
        response = self.client.get(url, data, format('json'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_car_detail(self):
        self.client.force_login(user=self.user)
        url = '/api/cars/'+str(self.car.id)+"/"
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {"name": "УАЗ 2078", "created_date": "2078-01-01", "added_date": date.today()}
        response = self.client.patch(url, data, format('json'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_detail_and_add_car(self):
        self.client.force_login(user=self.user)
        url = '/api/users/'+str(self.user.id)+"/"
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {"username": "new_user", "email": "new_user@mail.ru", "password": "new_pass_123456", "cars": [{"id":"1"}]}
        response = self.client.put(url, data, format('json'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

