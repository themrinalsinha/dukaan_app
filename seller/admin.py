from django.contrib import admin

# Register your models here.
from .models import SellerAccount, Store

admin.site.register(SellerAccount)
admin.site.register(Store)
