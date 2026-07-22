from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user_name               = serializers.CharField(source='user.username', read_only=True)
    court_name              = serializers.CharField(source='court.name', read_only=True)

    class Meta:
        model               = Review
        fields              = ['id', 'user', 'user_name', 'court', 'court_name', 'rating', 'comment', 'is_approved', 'created_at']
        read_only_fields    = ['created_at', 'updated_at', 'id', 'user', 'court', 'is_approved']