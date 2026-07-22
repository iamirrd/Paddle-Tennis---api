from django.urls import path
from .api_views import CourtViewSet, CourtImageViewSet, ScheduleViewSet, TimeSlotViewSet, BlockedSlotViewSet, CourtPricingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courts', CourtViewSet)
router.register(r'court-images', CourtImageViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'timeslots', TimeSlotViewSet)
router.register(r'blockedslots', BlockedSlotViewSet)
router.register(r'court-pricings', CourtPricingViewSet)

urlpatterns = router.urls