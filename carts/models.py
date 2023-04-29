from django.db import models
from store.models import Product

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=500, blank=True)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.cart_id
    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.quantity * self.product.price

    def __str__(self) -> str:
        return self.product