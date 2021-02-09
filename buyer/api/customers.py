from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import CustomerAccountSerializer

class CustomerAccountCreateView(GenericAPIView):
    serializer_class = CustomerAccountSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

customer_account_create_view = CustomerAccountCreateView.as_view()
