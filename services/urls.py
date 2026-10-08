from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ServiceViewSet, OrderViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('services', ServiceViewSet, basename='service')
router.register('orders', OrderViewSet, basename='order')

urlpatterns = router.urls