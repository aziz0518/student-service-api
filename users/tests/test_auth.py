import pytest
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
class TestAuthenticationAPI:

    def test_user_registration_success(self, api_client):
        url = reverse('auth_register')
        payload = {
            'username': 'newstudent',
            'email': 'student@example.com',
            'password': 'StrongPassword123',
            'password_confirm': 'StrongPassword123',
            'role': 'student',
            'phone_number': '+998901234567'
        }
        response = api_client.post(url, payload, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.filter(username='newstudent').exists()

    def test_jwt_login_success(self, api_client):
        from users.factories import UserFactory
        user = UserFactory(username='testlogin', role='student')

        url = reverse('token_obtain_pair')
        payload = {
            'username': 'testlogin',
            'password': 'password123'
        }
        response = api_client.post(url, payload, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data
        assert 'refresh' in response.data