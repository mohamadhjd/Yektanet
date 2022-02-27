from django.urls import path
from rest_framework.generics import ListCreateAPIView

from advertiser_management import views
from django.views.generic.base import RedirectView
from .models import Ad, Advertiser
from .serializer import AdvertiserSerializer

urlpatterns = [
    path('', views.ShowAd.as_view()),
    path('save_ad', views.SaveAd.as_view()),
    path('detail_ad', views.DetailReport.as_view()),
    path('advertiser', views.AdvertiserList.as_view()),
    path('ad', views.AdList.as_view()),
    path('click', views.ClickList.as_view()),
    path('view', views.ViewList.as_view()),
    path('ad/<pk>', views.LinkAd.as_view()),
]
