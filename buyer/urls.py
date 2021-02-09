from django.urls import path
from .api import customer_order_view

urlpatterns = [
    path('store/<str:store_slug>/', customer_order_view),
]
