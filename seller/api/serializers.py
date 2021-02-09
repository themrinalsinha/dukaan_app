from secrets import token_hex
from seller.models.account import Store

from django.db import IntegrityError
from django.utils.text import slugify
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from manager.utils import get_store_link
from seller.models import SellerAccount

class SellerAccountSerializer(serializers.ModelSerializer):
    otp = serializers.CharField(required=True)
    auth_token = serializers.CharField(required=False)
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


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ["name", "address"]

    def to_representation(self, instance):
        data = {
            "store_name": instance.name,
            "address": instance.address,
            "store_id": instance.slug,
            "store_link": instance.meta_info.get("store_link"),
        }
        return data

    def create(self, validated_data):
        request = self.context["request"]
        _store_slug = slugify(f"{request.account.mobile} {validated_data.get('name')}")

        validated_data.setdefault("seller", request.account)
        validated_data.setdefault("slug", _store_slug)
        validated_data.setdefault(
            "meta_info", {"store_link": get_store_link(request, _store_slug)}
        )

        try:
            return super().create(validated_data)
        except IntegrityError:
            raise ValidationError("Account with same store name already exists")
