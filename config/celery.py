import os
from celery import Celery

# Django settings modulini ko'rsatamiz
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('student_service')

# Sozlamalarni settings.py'dan 'CELERY_' prefiksi bilan o'qiydi
app.config_from_object('django.conf:settings', namespace='CELERY')

# Barcha registratsiya qilingan app'lardagi tasks.py fayllarini avtomatik topadi
app.autodiscover_tasks()