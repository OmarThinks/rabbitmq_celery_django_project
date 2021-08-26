"""
Original File: https://github.com/veryacademy/YT-Django-Celery-Series-Intro-Install-Run-Task/blob/master/app1/tasks.py

celery -A _app worker -l info 
# Mac or Linux


celery -A _app worker --pool=solo -l info
# Windows

"""
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from rest_framework import viewsets
import time
from .serializers import ProductSerializer
from .models import Product



@shared_task
def add(x, y):
	return x + y


@shared_task
def celery_perform_create_product(validated_data):
	p = Product.objects.create(**validated_data)
	return "Created product sucessfully "+str(p)


@shared_task
def celery_perform_update():
	pass

@shared_task
def celery_perform_delete():
	pass
