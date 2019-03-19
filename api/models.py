from django.db import models

# Create your models here.


class Message(models.Model):
    user_message = models.CharField(max_length=200)

class Phone(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=400)
    display = models.FloatField()
    storage = models.CharField(max_length=20)
    memory = models.CharField(max_length=20)
    price = models.IntegerField()
    is_cart = models.IntegerField()
    is_wishlist = models.IntegerField()
    is_history = models.IntegerField()
