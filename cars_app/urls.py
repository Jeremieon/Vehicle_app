from django.urls import path,include
from rest_framework.routers import DefaultRouter
from cars_app import views



router =  DefaultRouter()
router.register(r'cars',views.VehicleViewSet)
router.register(r'cat',views.CategoryViewSet)



urlpatterns = [
    path('', include(router.urls)),
]