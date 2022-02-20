from django.db import models


class AdvertiserManager(models.Manager):
    def get_by_id(self, advertiserID):
        qs = self.get_queryset().filter(id=advertiserID)
        return qs


class Advertiser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    objects = AdvertiserManager()

    def __str__(self):
        return self.name


class Ad(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(default="static_cdn/DEBR0551.JPG", upload_to='upload/')
    link = models.URLField(max_length=500)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    advertiser = models.ForeignKey(Advertiser, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
