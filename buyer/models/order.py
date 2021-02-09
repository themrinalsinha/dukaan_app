from django.db import models
from seller.models import Product
from buyer.models import CustomerAccount

class Order(models.Model):
    customer = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)
    meta_info = models.JSONField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    @property
    def reference(self):
        return f"O{self.id:04}"

    def __str__(self) -> str:
        return f"{self.reference}"

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    store_link = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.order.reference} --> {self.product}"
