from django.shortcuts import render
from rest_framework import generics
from .serializations import *
from .models import *

# Create your views here.

class ProductCategoryView(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerialization

class ProductCreateCategoryView(generics.CreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerialization

class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialization

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialization

