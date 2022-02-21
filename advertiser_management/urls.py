from django.urls import path
from . import views
from .models import Ad

urlpatterns = [
    path('', views.show_ad),
    path('save_ad', views.save_ad),
]