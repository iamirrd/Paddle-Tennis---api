from .models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password     = serializers.CharField(write_only=True, required=True , validators=[validate_password])
    password2    = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model   = User
        fields  = ['username', 'email', 'password', 'password2' , 'phone' ]
        
    def validate(self, attrs):
        """بررسی مطابقت رمزها"""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                "password": "رمزهای عبور مطابقت ندارند"
            })
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone']
        read_only_fields = ['id']


class ChangePasswordSerializer(serializers.Serializer):
    
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
    confirm_password = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "رمزهای عبور مطابقت ندارند"})
        return attrs