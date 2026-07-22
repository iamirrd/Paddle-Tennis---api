from django.shortcuts import render
from .serializers import PaymentSerializer
from .models import Payment
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter , OrderingFilter

class PaymentViewSet(ModelViewSet):
    queryset             = Payment.objects.all()
    serializer_class     = PaymentSerializer
    filter_backends      = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    permission_classes   = (IsAuthenticated, IsOwnerOrReadOnly)
    filterset_fields     = ('reservation' , 'status')
    search_fields        = ('user__username' , 'reservation__court__name')
    ordering_fields      = ('created_at', 'amount')
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Payment.objects.all()
        return Payment.objects.filter(reservation__user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)