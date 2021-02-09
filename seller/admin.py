from django.contrib import admin

# Register your models here.
from .models import SellerAccount, Store, Category, Product

admin.site.register(SellerAccount)
admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Product)
