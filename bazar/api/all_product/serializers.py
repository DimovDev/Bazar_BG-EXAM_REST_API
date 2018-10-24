from rest_framework import serializers
from all_product.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
           'owner', 'id',  'category', 'name', 'slug', 'image', 'description', 'price', 'stock', 'available', 'created',
            'updated',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'name', 'slug',)


# class AllProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AllProduct
#         fields = (
#             'id', 'name', 'slug', 'image', 'description', 'price', 'stock', 'available', 'created',
#             'updated',)
