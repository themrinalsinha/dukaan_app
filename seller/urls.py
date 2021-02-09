from django.urls import path, include
from .api import seller_account_create_view

urlpatterns = [
    path('create_account', seller_account_create_view),
]
