from seller.models.account import Store
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

from manager.auth import SellerAuth
from seller.models import Product

from .serializers import ProductSerializer

class ProductView(GenericAPIView):
    parser_classes = [MultiPartParser]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["store"] = Store.objects.get(slug=self.kwargs.get("store_slug"))
        return context

    def get(self, request, *args, **kwargs):
        store_slug = kwargs.get("store_slug")
        queryset = self.get_queryset().filter(store__slug=store_slug)
        products = ProductSerializer(queryset, many=True)
        return Response(products.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

product_view = ProductView.as_view()
