from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model

from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    paid  = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Order {self.id}'


    def total_price(self):
        return sum(item.get_cost() for item in self.items.all())




class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f'{self.product.title} {self.quantity} {self.price}'


    def get_cost(self):
        return self.price * self.quantity
