from secrets import token_hex

from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from seller.models import SellerAccount

class SellerAccountSerializer(serializers.ModelSerializer):
    otp = serializers.CharField(required=True)

    class Meta:
        model = SellerAccount
        fields = '__all__'

    def to_representation(self, instance):
        data = {
            "mobile": instance.mobile,
            "auth_token": instance.auth_token
        }
        return data

    def create(self, validated_data):
        otp = validated_data.pop('otp', None)

        if not otp:
            raise ValidationError("otp not provided")

        validated_data.setdefault('auth_token', token_hex(16))
        validated_data.setdefault('is_verified', True)
        try:
            instance = SellerAccount.objects.create(**validated_data)
        except IntegrityError:
            raise ValidationError("User Already Exists")

        return instance
