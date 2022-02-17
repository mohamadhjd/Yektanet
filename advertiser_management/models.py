from django.db import models


class Advertiser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    clicks = models.IntegerField()
    views = models.IntegerField()


class Ad(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField()
    link = models.URLField()
    clicks = models.IntegerField()
    views = models.IntegerField()
    advertiser = models.ForeignKey(Advertiser, models.SET_NULL, blank=True, null=True,)
