from django.contrib import admin

# Register your models here.
from .models import Ad, Advertiser

admin.site.register(Advertiser)
admin.site.register(Ad)