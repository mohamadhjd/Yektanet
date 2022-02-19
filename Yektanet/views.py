from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreateAd
from advertiser_management.models import Advertiser, Ad


def show_ad(request):
    advertiser = Advertiser.objects.all()
    ad = Ad.objects.all()
    context = {
        'ad': ad,
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
        ad = Ad.objects.create(advertiser=advertiser, title=title, link=link, image=image)
        return redirect(show_ad)

    return render(request, 'save_ad.html', context)


def detail_ad(request, *args, **kwargs):
    adId = kwargs['pk']
    ad = Ad.objects.filter(id=adId).first()
    advertiser = ad.advertiser
    advertiser.clicks += 1
    advertiser.views += 1
    ad.clicks += 1
    ad.views += 1
    ad.save()
    advertiser.save()
    context = {
        'ad': ad,
    }

    return render(request, 'detail_ad.html', context)
