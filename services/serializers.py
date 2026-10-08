from rest_framework import serializers
from .models import Category, Service, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Service
        fields = ('id', 'title', 'category', 'category_name', 'description', 'price', 'is_active', 'created_at')


class OrderSerializer(serializers.ModelSerializer):
    student_username = serializers.ReadOnlyField(source='student.username')
    service_title = serializers.ReadOnlyField(source='service.title')

    class Meta:
        model = Order
        fields = ('id', 'student', 'student_username', 'service', 'service_title', 'status', 'file', 'created_at', 'updated_at')
        read_only_fields = ('student', 'status')