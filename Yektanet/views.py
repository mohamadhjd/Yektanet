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
    create_ad = CreateAd()
    context = {
        'form': create_ad
    }
    if create_ad.is_valid():
        advertiserID = create_ad.cleaned_data.get('advertiserID')
        return redirect('')
    return render(request, 'save_ad.html', context)
