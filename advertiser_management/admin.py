from django.contrib import admin

# Register your models here.
from .models import Ad, Advertiser, Click, View


class AdAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'advertiser', 'approve')
    list_filter = ('approve',)
    search_fields = ['title']

    class Meta:
        model = Ad


admin.site.register(Advertiser)
admin.site.register(Ad, AdAdmin)
admin.site.register(Click)
admin.site.register(View)
