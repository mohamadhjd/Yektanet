from django.views.generic.base import TemplateView, RedirectView
from django.shortcuts import render, redirect
from .forms import CreateAd
from .models import Advertiser, Ad, View, Click
from django.views.generic.edit import FormView
import datetime


class ShowAd(TemplateView):
    template_name = 'show_ad.html'

    def get_context_data(self, *args, **kwargs):
        request = self.request
        advertisers = Advertiser.objects.all()
        ads = Ad.objects.filter(approve=True)
        for advertiser in advertisers:
            advertiser.views += 1
            advertiser.save()
        for ad in ads:
            view = View.objects.create(ad=ad, time=datetime.datetime.now(), ip=request.META)
            view.save()
        context = {
            'advertiser': Advertiser.objects.all(),
            'ad': Ad.objects.filter(approve=True),
        }
        return context


class SaveAd(FormView, TemplateView):
    template_name = 'save_ad.html'
    form_class = CreateAd
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        create_ad = CreateAd(self.request.POST, self.request.FILES)
        context = super().get_context_data(**kwargs)
        context['form'] = create_ad
        return context

    def form_valid(self, form):
        advertiserID = form.cleaned_data.get('advertiserID')
        title = form.cleaned_data.get('title')
        link = form.cleaned_data.get('link')
        image = form.cleaned_data.get('image')
        advertiser = Advertiser.objects.get_by_id(advertiserID).first()
        if Advertiser.objects.get_by_id(advertiserID).exists():
            Ad.objects.create(advertiser=advertiser, title=title, link=link, image=image)
        else:
            raise ValueError('this advertiser dose not exist')
        return super().form_valid(form)


class LinkAd(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        request = self.request
        ad = Ad.objects.filter(id=kwargs['pk']).first()
        advertiser = ad.advertiser
        advertiser.clicks += 1
        advertiser.save()
        click = Click.objects.create(ad=ad, time=datetime.datetime.now(), ip=request.META)
        click.save()
        return ad.link


class DetailReport(TemplateView):
    template_name = 'detail_report.html'

    def get_context_data(self, *args, **kwargs):
        ads = Ad.objects.filter(approve=True)
        advertisers = Advertiser.objects.all()
        context = super().get_context_data(**kwargs)
        time_click = []
        title = []
        counted = []
        for ad in ads:
            clicks = Click.objects.filter(ad=ad.id)
            for i in range(24):
                count = 0
                for click in clicks:
                    x = datetime.datetime.replace(click.time)
                    if int(x.strftime("%H")) <= i:
                        count += 1
            title.append(ad.title)
            counted.append(count)
            time_click.append(x.strftime('%H'))

        views = View.objects.order_by('time').reverse()
        view = []
        title_view = []
        time_view = []
        for ad in ads:
            count = 0
            for v in views:
                if v.ad == ad:
                    count += 1
            view.append(count)
        for v in views:
            x = datetime.datetime.replace(v.time)
            time_view.append(x.strftime('%X'))
            title_view.append(v.ad.title)

        time_difference = []
        for ad in ads:
            clicks = Click.objects.filter(ad=ad)
            views = View.objects.filter(ad=ad)
            for v in views:
                for click in clicks:
                    if v.ip == click.ip:
                        difference = v.time - click.time
                        time_difference.append(difference)

        context = {
            'title': title,
            'count': counted,
            'time_click': time_click,

            'view': view,
            'time_view': time_view,
            'title_view': title_view,

            'time_difference': time_difference
        }
        return context
