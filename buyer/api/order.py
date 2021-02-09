from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from manager.auth import BuyerAuth
from manager.redis_store import RedisStore

from seller.models import Product
from seller.api.serializers import ProductSerializer


_store = RedisStore()
class CustomerOrderView(GenericAPIView):
    authentication_classes = [BuyerAuth]

    def get(self, request, *args, **kwargs):
        customer, params = None, request.query_params

        action = params.get("action")
        product_id = params.get("product_id")
        store_slug = kwargs.get("store_slug")

        # validating action and product_id
        if not action:
            raise ValidationError("'action' is mandatory")

        # validating product
        if product_id:
            product = Product.objects.filter(id=product_id, store__slug=store_slug)
            if not product.exists():
                raise ValidationError("Product do not belong to the store")

        if hasattr(request, 'account'):
            customer = request.account.auth_token

        elif hasattr(request, 'unauthorized_account'):
            customer = request.unauthorized_account

        if action == 'add':
            _store.add_to_cart(customer, product_id)
            return Response({"detail": f"Product {product_id} added to cart."})

        if action == 'display':
            product_ids = _store.get_cart(customer)
            product_ids = [k.decode() for k in product_ids]
            _products = Product.objects.filter(id__in=product_ids)
            data = ProductSerializer(_products, many=True).data
            return Response(data, status=status.HTTP_200_OK)

        if action == 'remove':
            _count = _store.remove_from_cart(customer, product_id)
            if _count > 0:
                return Response({"detail": f"Product {product_id} removed from cart."})
            return Response({"detail": f"Product {product_id} do not exist in cart."})

customer_order_view = CustomerOrderView.as_view()
