from rest_framework import serializers
from all_product.models import Product, Category, Location


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = (
            'owner', 'id', 'category', 'location', 'name', 'slug', 'image', 'description', 'price', 'stock',
            'available',
            'created',
            'updated',)
        read_only_fields = ['owner']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug',)


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'slug',)
# class AllProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AllProduct
#         fields = (
#             'id', 'name', 'slug', 'image', 'description', 'price', 'stock', 'available', 'created',
#             'updated',)
