from rest_framework import serializers, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from manager.auth import SellerAuth

from seller.models import Store
from .serializers import SellerAccountSerializer, StoreSerializer


class SellerAccountCreateView(GenericAPIView):
    serializer_class = SellerAccountSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

seller_account_create_view = SellerAccountCreateView.as_view()


class SellerStoreView(GenericAPIView):
    serializer_class = StoreSerializer
    authentication_classes = [SellerAuth]

    def get_queryset(self):
        return Store.objects.filter(seller=self.request.account)

    def get(self, request, *args, **kwargs):
        _data = self.get_queryset()
        serializer = self.get_serializer(_data, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


seller_store_view = SellerStoreView.as_view()
