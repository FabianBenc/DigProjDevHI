from django.db import models
from django.contrib.auth.models import User


class Color(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    torso_color = models.CharField(max_length=7)
    pockets_color = models.CharField(max_length=7)
    left_sleeve_color = models.CharField(max_length=7)
    right_sleeve_color = models.CharField(max_length=7)
    is_in_shop = models.BooleanField(default=False)

class Size(models.Model):
    size = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=255)
    colors = models.ForeignKey(Color, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.ManyToManyField(Product,through='OrderDetails')

class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

