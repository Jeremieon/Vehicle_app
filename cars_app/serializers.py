from rest_framework import serializers
from .models import Vehicle,Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id','make','model','year','category','price_usd','country_made','wheels','horsepower','weight','color','fuel_type']

