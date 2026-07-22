from django.urls import path
from .api_views import ReservationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'reservations', ReservationViewSet)

urlpatterns = router.urls