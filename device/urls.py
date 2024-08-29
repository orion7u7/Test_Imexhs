from django.urls import path, include
from rest_framework.routers import DefaultRouter
from device import views

router = DefaultRouter()
router.register(r'elements', views.DeviceDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]