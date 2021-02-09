from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import SellerAccountSerializer


class SellerAccountCreateView(GenericAPIView):
    serializer_class = SellerAccountSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

seller_account_create_view = SellerAccountCreateView.as_view()
