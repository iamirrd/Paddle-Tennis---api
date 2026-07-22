from rest_framework import serializers
from .models import Court, CourtImage, Schedule, TimeSlot, BlockedSlot, CourtPricing


class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = ('id', 'name', 'address', 'city', 'max_players', 'base_price_per_hour', 'is_active', 'description')
        read_only_fields = ('created_at', 'updated_at' , 'id')
        
class CourtImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtImage
        fields = ('image', 'is_primary' , 'court')
        read_only_fields = ('created_at', 'updated_at' , 'id')
        
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'court', 'day_of_week', 'start_time', 'end_time', 'is_active')
        read_only_fields = ('created_at', 'updated_at' , 'id')
        
class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ('id', 'court', 'date', 'start_time', 'end_time', 'status')
        read_only_fields = ('created_at', 'updated_at' , 'id')
        
class BlockedSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockedSlot
        fields = ('id', 'court', 'date', 'start_time', 'end_time', 'description', 'is_active')
        read_only_fields = ('created_at', 'updated_at' , 'id')
        
class CourtPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtPricing
        fields = ('id', 'court', 'pricing_type', 'price_multiplier', 'is_active')
        read_only_fields = ('created_at', 'updated_at' , 'id')