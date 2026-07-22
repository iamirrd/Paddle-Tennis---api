
from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    user_name           = serializers.CharField(source='user.username', read_only=True)
    court_name          = serializers.CharField(source='court.name', read_only=True)
    slot_info           = serializers.CharField(source='slot.__str__', read_only=True)

    class Meta:
        model            = Reservation
        fields           = ['id', 'user', 'user_name', 'court', 'court_name', 'slot', 'slot_info', 'total_price', 'players_count', 'status', 'is_paid', 'created_at']
        read_only_fields = ['created_at', 'updated_at', 'id', 'user', 'total_price', 'status', 'is_paid']