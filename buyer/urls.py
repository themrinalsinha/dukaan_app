from django.urls import path
from .api import customer_order_view, customer_account_create_view

urlpatterns = [
    path('create_account', customer_account_create_view),
    path('store/<str:store_slug>/', customer_order_view),
]
