import datetime

from advertiser_management.models import Ad, Click


class CreateClicksMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        id = request.path

        if '/ad/detail/' in request.path:
            print(id)
            ad = Ad.objects.filter(id=id[4]).first()
            advertiser = ad.advertiser
            advertiser.clicks += 1
            advertiser.save()
            click = Click.objects.create(ad=ad, time=datetime.datetime.now(), ip=request.META.get('REMOTE_ADDR'))

        response = self.get_response(request)
        return response
