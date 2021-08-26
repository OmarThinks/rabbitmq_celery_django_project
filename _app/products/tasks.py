# Original File: https://github.com/veryacademy/YT-Django-Celery-Series-Intro-Install-Run-Task/blob/master/app1/tasks.py


"""
celery -A _app worker -l info

"""




from __future__ import absolute_import, unicode_literals

from celery import shared_task
from rest_framework import viewsets
import time

@shared_task
def add(x, y):
	return x + y


@shared_task
def celery_perform_create(self, serializer):
	print("Will Create", flush=True)
	#time.sleep(15)
	viewsets.ModelViewSet.perform_create(self,serializer)
	print("Created", flush=True)
	return "Celery is done"


@shared_task
def celery_perform_update():
	pass

@shared_task
def celery_perform_delete():
	pass
