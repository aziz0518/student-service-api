from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, permissions
from .models import Category, Service, Order
from .serializers import CategorySerializer, ServiceSerializer, OrderSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdmin
from .tasks import send_order_notification_task

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    # 15 minut davomida keshda saqlash
    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.select_related('category').filter(is_active=True)
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]

    # 10 minut davomida keshda saqlash
    @method_decorator(cache_page(60 * 10))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.select_related('student', 'service')
        if user.is_staff or user.role == 'admin':
            return queryset
        return queryset.filter(student=user)

    def perform_create(self, serializer):
        order = serializer.save(student=self.request.user)
        # Celery vazifasini fon rejimida (.delay()) chaqiramiz
        send_order_notification_task.delay(
            order_id=order.id,
            user_email=order.student.email,
            service_title=order.service.title
        )