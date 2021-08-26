# Original File: https://github.com/veryacademy/YT-Django-Celery-Series-Intro-Install-Run-Task/blob/master/app1/tasks.py

from __future__ import absolute_import, unicode_literals

from celery import shared_task

@shared_task
def add(x, y):
	return x + y


@shared_task
def celery_perform_create():
	pass

@shared_task
def celery_perform_update():
	pass

@shared_task
def celery_perform_delete():
	pass
