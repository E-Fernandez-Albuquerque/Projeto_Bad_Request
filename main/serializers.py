from rest_framework import serializers
from .models import Product, Person, Contact

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price')