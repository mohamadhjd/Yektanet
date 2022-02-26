from django.urls import path
from advertiser_management import views
from django.views.generic.base import RedirectView
from .models import Ad

urlpatterns = [
    path('', views.ShowAd.as_view()),
    path('save_ad', views.SaveAd.as_view()),
    path('detail_ad', views.DetailReport.as_view()),
    path('get_ad_data', views.get_ad_data),
    path('get_advertiser_data', views.get_advertiser_data),
    path('get_click_data', views.get_click_data),
    path('get_view_data', views.get_view_data),
    path('ad/<pk>', views.LinkAd.as_view()),
]
