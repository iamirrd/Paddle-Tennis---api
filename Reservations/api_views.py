from django.shortcuts import render
from .serializers import ReservationSerializer
from .models import Reservation
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter , OrderingFilter



class ReservationViewSet(ModelViewSet):
    queryset             = Reservation.objects.all()
    serializer_class     = ReservationSerializer
    filter_backends      = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    permission_classes   = (IsAuthenticated, IsOwnerOrReadOnly)
    filterset_fields     = ('court' , 'slot')
    search_fields        = ('user__username' , 'court__name')
    ordering_fields      = ('created_at', 'total_price')