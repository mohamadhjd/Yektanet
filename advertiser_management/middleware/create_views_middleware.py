import datetime

from advertiser_management.models import Ad, View, Advertiser


class CreateViewsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/':
            ads = Ad.objects.filter(approve=True)
            for ad in ads:
                advertisers = Advertiser.objects.filter(name=ad.advertiser).first()
                advertisers.views += 1
                advertisers.save()
            for ad in ads:
                view = View.objects.create(ad=ad, time=datetime.datetime.now(), ip=request.META.get('REMOTE_ADDR'))
                view.save()

        response = self.get_response(request)
        return response

