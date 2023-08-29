from rest_framework import serializers
from .models import Vehicle,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class VehicleSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Vehicle
        fields = ['id','make','model','year','category','price_usd','country_made','wheels','horsepower','weight','color','fuel_type']

