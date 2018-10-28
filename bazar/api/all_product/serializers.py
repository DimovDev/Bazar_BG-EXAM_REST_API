from rest_framework import serializers
from all_product.models import Product, Category, Location


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'owner', 'id', 'category', 'location', 'phone_number', 'name', 'image', 'description', 'price', 'stock',
            'available',
            'created',
            'updated',)
        read_only_fields = ['owner']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name','image')


class AllProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id', 'owner', 'location', 'phone_number', 'category', 'name', 'image', 'description', 'price', 'stock',
            'available',
            'created', 'updated')
        read_only_fields = ['owner', ]
