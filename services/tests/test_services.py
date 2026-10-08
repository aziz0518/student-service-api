import pytest
from unittest.mock import patch
from django.urls import reverse
from rest_framework import status
from services.factories import ServiceFactory
from users.factories import UserFactory


@pytest.mark.django_db
class TestServicesAndOrders:

    def test_student_can_create_order_and_triggers_celery(self, api_client):
        # 1. Ma'lumotlarni tayyorlash
        student = UserFactory(role='student')
        service = ServiceFactory()
        
        # Student sifatida JWT authenticate qilish
        api_client.force_authenticate(user=student)

        url = reverse('order-list')
        payload = {'service': service.id}

        # 2. Celery task'ni mock qilamiz (haqiqiy Redis/Celery'ni kutmaslik uchun)
        with patch('services.tasks.send_order_notification_task.delay') as mock_task:
            response = api_client.post(url, payload, format='json')

            # 3. Tekshiruvlar
            assert response.status_code == status.HTTP_201_CREATED
            assert response.data['student'] == student.id
            assert response.data['service'] == service.id

            # Celery task to'g'ri argumentlar bilan chaqirilganini tasdiqlash
            mock_task.assert_called_once_with(
                order_id=response.data['id'],
                user_email=student.email,
                service_title=service.title
            )

    def test_unauthenticated_user_cannot_create_order(self, api_client):
        service = ServiceFactory()
        url = reverse('order-list')
        payload = {'service': service.id}

        response = api_client.post(url, payload, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED