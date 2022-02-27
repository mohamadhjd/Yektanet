from rest_framework import serializers
from .models import Ad, Advertiser, Click, View


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = '__all__'

    def create(self, validated_data):
        return Advertiser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.clicks = validated_data.get('clicks', instance.clicks)
        instance.views = validated_data.get('views', instance.views)
        instance.save()
        return instance


class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = '__all__'


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = '__all__'
