from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, db_index=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    mrp = models.PositiveIntegerField()
    sale_price = models.PositiveIntegerField()
    image = models.FileField(upload_to='catlog/')
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
