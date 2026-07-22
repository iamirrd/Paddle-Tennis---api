from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    user_name             = serializers.CharField(source='user.username', read_only=True)
    reservation_info      = serializers.CharField(source='reservation.__str__', read_only=True)

    class Meta:
        model             = Payment
        fields            = ['id', 'user', 'user_name', 'reservation', 'reservation_info', 'amount', 'status', 'tracking_code', 'created_at']
        read_only_fields  = ['created_at', 'updated_at', 'id', 'user', 'reservation', 'status']