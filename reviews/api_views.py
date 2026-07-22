from django.shortcuts import render
from .serializers import ReviewSerializer
from .models import Review
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter , OrderingFilter


class ReviewViewSet(ModelViewSet):
    queryset             = Review.objects.all()
    serializer_class     = ReviewSerializer
    filter_backends      = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    permission_classes   = (IsAuthenticated, IsOwnerOrReadOnly)
    filterset_fields     = ('court' , 'rating')
    search_fields        = ('user__username' , 'court__name')    
    ordering_fields      = ('created_at', 'rating')