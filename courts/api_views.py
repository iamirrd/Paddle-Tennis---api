from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Court, CourtImage, Schedule, TimeSlot, BlockedSlot, CourtPricing
from .serializers import CourtSerializer, CourtImageSerializer, ScheduleSerializer, TimeSlotSerializer, BlockedSlotSerializer, CourtPricingSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter , OrderingFilter
from .permissions import AdminWriteOthersReadOnly

class BaseViewSet(ModelViewSet):
    filter_backends     = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    permission_classes  = (AdminWriteOthersReadOnly ,)

class CourtViewSet(BaseViewSet):
    queryset            = Court.objects.all()
    serializer_class    = CourtSerializer
    filterset_fields    = ('city', 'is_active' , 'court_type')
    search_fields       = ('name', 'address')
    ordering_fields     = ('name', 'base_price_per_hour')
    
    
class CourtImageViewSet(BaseViewSet):
    queryset            = CourtImage.objects.all()
    serializer_class    = CourtImageSerializer
    filterset_fields    = ('is_primary' , 'court')
    ordering_fields     = ('court',)
    search_fields       = ('court__name',)
    
class ScheduleViewSet(BaseViewSet):
    queryset            = Schedule.objects.all()
    serializer_class    = ScheduleSerializer
    filterset_fields    = ('court' , 'day_of_week')
    ordering_fields     = ('day_of_week', 'start_time')
    search_fields       = ('court__name',)
    
class TimeSlotViewSet(BaseViewSet):
    queryset            = TimeSlot.objects.all()
    serializer_class    = TimeSlotSerializer
    filterset_fields    = ('court' , 'date')
    ordering_fields     = ('date', 'start_time')
    search_fields       = ('court__name',)
    
class BlockedSlotViewSet(BaseViewSet):
    queryset            = BlockedSlot.objects.all()
    serializer_class    = BlockedSlotSerializer
    filterset_fields    = ('court' , 'date')
    ordering_fields     = ('date', 'start_time')
    search_fields       = ('court__name',)
    
class CourtPricingViewSet(BaseViewSet):
    queryset            = CourtPricing.objects.all()
    serializer_class    = CourtPricingSerializer
    filterset_fields    = ('court' , 'pricing_type')
    ordering_fields     = ('court',)
    search_fields       = ('court__name',)