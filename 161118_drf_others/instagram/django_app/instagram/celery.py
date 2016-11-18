import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instagram.settings')

app = Celery('instagram')