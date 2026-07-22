from django.urls import path
from .api_views import PaymentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'payments', PaymentViewSet)

urlpatterns = router.urls