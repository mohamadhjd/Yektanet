from celery import shared_task
import time

@shared_task
def celery_task(counter):
    email = "rezahajiabdi78@gmail.com"
    time.sleep(30)
    return '{} Done!'.format(counter)


@shared_task
def send_notifiction():
     print('‘Here I\’m’')
