from cars_app.models import Category,Vehicle
from cars_app.serializers import VehicleSerializer,CategorySerializer
from rest_framework import viewsets

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
