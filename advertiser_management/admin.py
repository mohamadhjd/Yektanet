from django.contrib import admin

# Register your models here.
from .models import Ad, Advertiser, Click, View, AdsReports


class AdAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'advertiser', 'approve')
    list_filter = ('approve',)
    search_fields = ['title']

    class Meta:
        model = Ad


class AdsReportsAdmin(admin.ModelAdmin):
    list_filter = ('daily', 'hourly')

    class Meta:
        model = AdsReports


admin.site.register(Advertiser)
admin.site.register(Ad, AdAdmin)
admin.site.register(Click)
admin.site.register(View)
admin.site.register(AdsReports, AdsReportsAdmin)

