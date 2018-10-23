from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework import viewsets



# class MyProductViewSet(viewsets.ModelViewSet):
#     authentication_classes = (TokenAuthentication,)
#
#     model = Product
#     serializer_class = ProductSerializer
#
#     def get_queryset(self):
#         qs = Product.objects.all()
#         qs = qs.filter(owner=self.request.user)
#         return qs
#
#
# class MyCategoryViewSet(viewsets.ModelViewSet):
#     model = Category
#     serializer_class = CategorySerializer
#
#     def get_queryset(self):
#         qs = Category.objects.all()
#         # qs = qs.filter(owner=self.request.user)
#         return qs
#
#
# class AllProductViewSet(viewsets.ModelViewSet):
#     model = Product
#     serializer_class = ProductSerializer
#
#     def get_queryset(self):
#         qs = Product.objects.all()
#         # qs = qs.filter(owner=self.request.user)
#         return qs
# # class MyCartViewSet(viewsets.ModelViewSet):
# #     model = Cart
# #     serializer_class = CartSerializer
# #
# #     def get_queryset(self):
# #         qs = Cart.objects.all()
# #         # qs = qs.filter(owner=self.request.user)
# #         return qs


@csrf_exempt
def product_list(request, owner):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        cart = Product.objects.all()
        serializer = ProductSerializer(cart, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def product_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """

    try:
        product = Product.objects.get(pk=pk)

    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)


@csrf_exempt
def category_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def category_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """

    try:
        category = Category.get(pk=pk)

    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        category.delete()
        return HttpResponse(status=204)
