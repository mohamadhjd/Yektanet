from datetime import datetime
import datetime
import task as task
from celery import shared_task, current_app
import time
from django.db.models import Count
from .models import Ad, Click, View, AdsReports


@shared_task
def daily_report():
    ads = Ad.objects.filter(approve=True)
    i = 0
    click_count = Click.objects.values('ad__id').filter(
        time__day=int(datetime.datetime.now().strftime('%d')) - 1).annotate(Count('ad__click')).values('ad__click__count')
    view_count = View.objects.values('ad__id').filter(
        time__day=int(datetime.datetime.now().strftime('%d')) - 1).annotate(Count('ad__view')).values('ad__view__count')
    for ad in ads:
        AdsReports.objects.create(
            count_click=click_count[i]["ad__click__count"], count_view=view_count[i]["ad__view__count"], ad=ad, daily=True)
        i += 1
    return 'Done!'


@shared_task()
def hourly_report():
    ads = Ad.objects.filter(approve=True)
    i = 0
    click_count = Click.objects.values('ad__id').filter(
        time__day=int(datetime.datetime.now().strftime('%H')) - 1).annotate(Count('ad__click')).values('ad__click__count')
    view_count = View.objects.values('ad__id').filter(
        time__day=int(datetime.datetime.now().strftime('%H')) - 1).annotate(Count('ad__view')).values('ad__view__count')
    for ad in ads:
        AdsReports.objects.create(
            count_click=click_count[i]["ad__click__count"], count_view=view_count[i]["ad__view__count"], ad=ad, hourly=True)
    return 'Done!'
