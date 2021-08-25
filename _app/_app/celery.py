
# File Source Code: https://github.com/veryacademy/YT-Django-Celery-Series-Intro-Install-Run-Task/blob/master/proj/celery.py
from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_app.settings')

app = Celery('_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()