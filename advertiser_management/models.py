from django.db import models


class AdvertiserManager(models.Manager):
    def get_by_id(self, advertiserID):
        qs = self.get_queryset().filter(id=advertiserID)
        return qs


class AdManager(models.Manager):
    def inc_clicks(self, adID):
        qs = self.get_queryset().filter(id=adID)
        return qs


class Advertiser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    clicks = models.IntegerField()
    views = models.IntegerField()
    objects = AdvertiserManager()

    def __str__(self):
        return self.name


class Ad(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, upload_to='upload/')
    link = models.CharField(max_length=200)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    advertiser = models.ForeignKey(Advertiser, models.SET_NULL, blank=True, null=True, )

    def __str__(self):
        return self.title
