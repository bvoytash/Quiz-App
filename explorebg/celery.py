from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'explorebg.settings')

app = Celery('explorebg')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
broker_connection_retry_on_startup = True
