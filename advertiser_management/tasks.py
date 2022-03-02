from datetime import datetime

import task as task
from celery import shared_task, current_app
import time
from django.db.models import Count
from .models import Ad, Click, View, DailyReport, HourlyReport


@shared_task
def daily_report():
    ads = Ad.objects.filter(approve=True)
    for ad in ads:
        click_count = Click.objects.filter(ad=ad, time__day=int(datetime.now().strftime('%d')) - 1).annotate(Count('ad'))
        view_count = View.objects.filter(ad=ad, time__day=int(datetime.now().strftime('%d')) - 1).annotate(Count('ad'))
        HourlyReport.objects.create(count_click=click_count, count_view=view_count, ad=ad)
    return 'Done!'


@shared_task()
def hourly_report():
    ads = Ad.objects.filter(approve=True)
    for ad in ads:
        click_count = Click.objects.filter(ad=ad, time__hour=int(datetime.now().strftime('%H'))-1).annotate(Count('ad'))
        view_count = View.objects.filter(ad=ad,  time__hour=int(datetime.now().strftime('%H'))-1).annotate(Count('ad'))
        HourlyReport.objects.create(count_click=click_count, count_view=view_count, ad=ad)
    return 'Done!'
