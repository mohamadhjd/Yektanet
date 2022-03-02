from django.urls import path
from rest_framework.generics import ListCreateAPIView

from advertiser_management import views
from django.views.generic.base import RedirectView
from .models import Ad, Advertiser
from .serializer import AdvertiserSerializer
from .views import AdvertiserViewSet

urlpatterns = [
    path('', views.ShowAd.as_view()),
    path('save_ad', views.SaveAd.as_view()),
    path('detail_ad', views.DetailReport.as_view()),
    path('advertisers', views.AdvertiserViewSet.as_view({'get': 'list'})),
    path('ads', views.AdViewSet.as_view({'get': 'list'})),
    path('clicks', views.ClickViewSet.as_view({'get': 'list'})),
    path('views', views.ViewViewSet.as_view({'get': 'list'})),
    path('advertisers/<pk>', views.AdvertiserViewSet.as_view({'get': 'retrieve'})),
    path('ads/<pk>', views.AdViewSet.as_view({'get': 'retrieve'})),
    path('clicks/<pk>', views.ClickViewSet.as_view({'get': 'retrieve'})),
    path('views/<pk>', views.ViewViewSet.as_view({'get': 'retrieve'})),
    path('ad/<pk>', views.LinkAd.as_view()),

]
