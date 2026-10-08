import factory
from services.models import Category, Service
from users.factories import UserFactory


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f'Category {n}')


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service

    title = factory.Sequence(lambda n: f'Service {n}')
    category = factory.SubFactory(CategoryFactory)
    price = 100.00
    is_active = True