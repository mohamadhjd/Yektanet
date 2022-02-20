from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_ad),
    path('save_ad', views.save_ad),
    path('<pk>', views.detail_ad),
]