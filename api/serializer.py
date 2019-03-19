from rest_framework import serializers
from .models import *



class MessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['user_message']
class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['id', 'name', 'image', 'price','is_wishlist', 'is_cart']