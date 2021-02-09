from django.db import models


class SellerAccount(models.Model):
    mobile = models.CharField(max_length=16, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    auth_token = models.CharField(max_length=512, unique=True)
    meta_info = models.JSONField(blank=True, null=True)

    def __str__(self) -> str:
        return self.mobile
