from django.urls import path,include
from rest_framework.routers import DefaultRouter
from cars_app import views



router =  DefaultRouter()
router.register(r'cat',views.VehicleViewSet,basename="vehicles")
router.register(r'cat',views.CategoryViewSet,basename="categories")



urlpatterns = [
    path('', include(router.urls)),
]