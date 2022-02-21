
from django.shortcuts import render, redirect
from .forms import CreateAd
from .models import Advertiser, Ad


def show_ad(request):
    advertiser = Advertiser.objects.all()
    ads = Ad.objects.all()
    for ad in ads:
        ad.views += 1
        ad.save()
    context = {
        'ad': ads,
        'advertiser': advertiser
    }
    return render(request, 'show_ad.html', context)


def save_ad(request):
    create_ad = CreateAd(request.POST, request.FILES)
    context = {
        'form': create_ad,
    }
    if create_ad.is_valid():
        advertiserID = create_ad.cleaned_data.get('advertiserID')
        title = create_ad.cleaned_data.get('title')
        link = create_ad.cleaned_data.get('link')
        image = create_ad.cleaned_data.get('image')
        advertiser = Advertiser.objects.get_by_id(advertiserID).first()
        if Advertiser.objects.get_by_id(advertiserID).exists():
            ad = Ad.objects.create(advertiser=advertiser, title=title, link=link, image=image)
            return redirect(show_ad)
        else:
            raise ValueError('this advertiser dose not exist')
    return render(request, 'save_ad.html', context)


def detail_ad(request, *args, **kwargs):
    adId = kwargs['pk']
    ad = Ad.objects.filter(id=adId).first()
    advertiser = ad.advertiser
    advertiser.clicks += 1
    ad.clicks += 1
    ad.save()
    advertiser.save()

    return redirect(ad.link)
