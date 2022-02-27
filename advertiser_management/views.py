from django.views.generic.base import TemplateView, RedirectView
from django.shortcuts import render, redirect
from .forms import CreateAd
from .models import Advertiser, Ad, View, Click
from django.views.generic.edit import FormView
import datetime
from django.db.models import Count
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializer import AdSerializer, AdvertiserSerializer, ClickSerializer, ViewSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class AdvertiserList(generics.ListCreateAPIView):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer
    authentication_classes([SessionAuthentication, BasicAuthentication])
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = AdvertiserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AdList(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    authentication_classes([SessionAuthentication, BasicAuthentication])
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = AdSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClickList(generics.ListCreateAPIView):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer
    authentication_classes([SessionAuthentication, BasicAuthentication])
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ClickSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ViewList(generics.ListCreateAPIView):
    queryset = View.objects.all()
    serializer_class = ViewSerializer
    authentication_classes([SessionAuthentication, BasicAuthentication])
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ViewSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ShowAd(TemplateView):
    template_name = 'show_ad.html'

    def get_context_data(self, *args, **kwargs):
        advertisers = Advertiser.objects.all()
        ads = Ad.objects.filter(approve=True)
        context = {
            'advertiser': advertisers,
            'ad': ads,
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
        return ad.link


class DetailReport(TemplateView):
    template_name = 'detail_report.html'

    def get_context_data(self, *args, **kwargs):
        request = self.request
        ads = Ad.objects.filter(approve=True)
        context = super().get_context_data(**kwargs)
        time_click = []
        title = []
        counted = []

        view = []
        title_view = []
        time_view = []
        time_difference = []

        for ad in ads:
            clicks = Click.objects.filter(ad=ad.id)
            count = clicks.count()
            counted.append(count)
            time_click.append(clicks.values('time'))
            title.append(ad.title)

            views = View.objects.order_by('time').reverse()
            views = views.filter(ad=ad)
            count = views.count()
            view.append(count)
            time_view.append(views.values('time'))
            title_view.append(views.values('ad'))

            clicks = Click.objects.filter(ad=ad)
            views = View.objects.filter(ad=ad)
            for click in clicks:
                views = views.filter(ip=click.ip).first()
                difference = views.time - click.time
                time_difference.append(difference)

        context = {
            'title': title,
            'count': counted,
            'time_click': time_click,

            'view': view,
            'time_view': time_view,
            'title_view': title_view,

            'time_difference': time_difference,
        }
        return context
