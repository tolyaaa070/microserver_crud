from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework import generics , viewsets

import requests
from rest_framework import generics, status
from rest_framework.exceptions import AuthenticationFailed
from .pagination import ProductPagination
class CategoryListViewSets(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryDetailViewSets(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryCreateViewSets(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryEditViewSets(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers
    # pagination_class = [ProductPagination]


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers

class ProductEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers

class SubcategoryEditViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubCategorySerializers

class SubcategoryCreateViewSet(generics.ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubCategorySerializers


class SubcategoryListViewSet(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubCategorySerializers

class SubcategoryDetailViewSet(generics.RetrieveAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubCategorySerializer


class ReviewsListViewSet(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers

class ReviewsDetailViewSet(generics.RetrieveAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers

class ReviewsEditViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers

class ReviewsCreateViewSet(generics.CreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers
    # permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers

    # def perform_create(self, serializer):
    #     serializer.save(owner_id=self.request.user.id)
    #


