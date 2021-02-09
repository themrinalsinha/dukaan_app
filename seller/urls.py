from django.urls import path, include
from .api import seller_account_create_view, seller_store_view

urlpatterns = [
    path('create_account', seller_account_create_view),
    path('stores', seller_store_view),
]
