import factory
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user_{n}')
    email = factory.LazyAttribute(lambda o: f'{o.username}@example.com')
    role = User.Role.STUDENT
    is_active = True

    @factory.post_generation
    def set_password(obj, create, extracted, **kwargs):
        password = extracted or 'password123'
        obj.set_password(password)
        if create:
            obj.save()