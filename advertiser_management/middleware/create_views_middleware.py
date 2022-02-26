import datetime

from advertiser_management.models import Ad, View, Advertiser


class CreateViewsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/':
            ads = Ad.objects.filter(approve=True)
            for ad in ads:
                ad.advertiser.views += 1
                ad.advertiser.save()
                View.objects.create(ad=ad, time=datetime.datetime.now(), ip=request.META.get('REMOTE_ADDR'))

        response = self.get_response(request)
        return response

