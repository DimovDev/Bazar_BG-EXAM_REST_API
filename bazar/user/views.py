from django.shortcuts import render

# Create your views here.
# Create your views here.
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
# POST metoda = uključuje serializers
# from api.all_shop.models import AllProduct
# from api.all_shop.serializers import AllProductSerializer
# from api.cart.cart import Cart
# # from api.cart.serializers import CartSerializer
# from api.shop.serializers import ProductSerializer, CategorySerializer
# # from api.cart.serializers import CartSerializer
# from api.shop.models import Product, Category
from .. import serializers
from . import serializers
from rest_framework import status

# Django viewset
from rest_framework import viewsets

from . import models
from . import permissions

from rest_framework import filters

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated


# Django rest_framework API response
class HelloApiView(APIView):
    """Test API View."""

    # dodaj serializers varijablu i referenciraj ju
    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    # metoda za POST response
    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)  # što god da request ima pošalji serializer objektu

        # provjeri da serializer ima ispravni data
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(
                name)  # {0, 1, 2} to je red po kojemu želim izlistati message koji je upisao korisnik
            return Response({'message': message})

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # sadrži lista grešaka koji nastanu

    # Http response
    def put(self, request, pk=None):
        """Handles updating object."""

        return Response({'method': 'put'})

    # Partialy update object
    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Delete an object."""

        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test APi ViewSet."""

    def list(self, request):
        """Return a hello message."""

        serializer = serializers.HelloSerializer  # isti serializer kao kod APIViw

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code.'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""

        serializer = serializers.HelloSerializer(data=request.data)  # isti serializer kao kod APIView

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)

            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method': 'GET'})

    # Http put method
    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object."""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)  # ostavi zarez jer varijbla mora biti vrste tuple
    permission_classes = (permissions.UpdateOwnProfile,)  # ostavi zarez
    filter_backends = (filters.SearchFilter,)  # ostavi zarez
    search_fields = ('name', 'email',)  # ostavi zarez


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create token."""

        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.StatusUpdate.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user_profile=self.request.user)


class MyProductViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)

    model = models.Product
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = models.Product.objects.all()
        # qs = qs.filter(owner=self.request.user)
        return qs


class MyCategoryViewSet(viewsets.ModelViewSet):
    model = models.Category
    serializer_class = CategorySerializer

    def get_queryset(self):
        qs = models.Category.objects.all()
        # qs = qs.filter(owner=self.request.user)
        return qs

#
# class AllProductViewSet(viewsets.ModelViewSet):
#     model = Product
#     serializer_class = ProductSerializer
#
#     def get_queryset(self):
#         qs = AllProduct.objects.all()
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