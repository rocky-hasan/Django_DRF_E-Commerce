from django.db import models
from mptt.models import TreeForeignKey,MPTTModel
# Create your models here.
class Category(MPTTModel):
    name=models.CharField(max_length=30)
    parent=TreeForeignKey("self",on_delete=models.PROTECT,null=True,blank=True)

    class MPTTMeta:
        order_insertion_by=["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=30)
    desc=models.TextField(blank=True)
    is_digital=models.BooleanField(default=False)
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE)
    category=TreeForeignKey(
        "Category",on_delete=models.SET_NULL, null=True, blank=True
        )

    def __str__(self):
        return self.name