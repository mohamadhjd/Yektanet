from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from .models import Ad

urlpatterns = [
    path('', views.ShowAd.as_view()),
    path('save_ad', views.SaveAd.as_view()),
    path('detail_ad', views.DetailReport.as_view()),
    path('ad/<pk>', views.LinkAd.as_view()),
]
