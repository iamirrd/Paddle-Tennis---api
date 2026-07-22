from django.urls import path
from .api_views import ReviewViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)

urlpatterns = router.urls