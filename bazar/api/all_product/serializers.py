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
        list_editable = ['price', 'stock', 'available']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug',)


class LocationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'slug',)


class AllProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = (
            'category',    'name', 'slug', 'image', 'description', 'price', 'stock', 'available', 'created',
            'updated',)
        list_editable = ['price', 'stock', 'available']
        read_only_fields = ['id', 'name', 'slug', 'image', 'description', 'price', 'stock', 'available', 'created',
                            'updated', ]
