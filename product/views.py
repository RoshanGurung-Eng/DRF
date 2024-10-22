from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializations import *
from .models import * 
from rest_framework.response import Response



# Create your views here.

# class ProductCategoryView(generics.ListAPIView):
#     queryset = ProductCategory.objects.all()
#    serializer_class = ProductCategorySerialization


def home(request):
    products = Product.objects.all()  # Fetch products for template rendering
    return render(request,'base.html', {'products': products})

class ProductCategoryView(viewsets.ViewSet):
    def list(self, request):
       queryset = ProductCategory.objects.all()
       serializer = ProductCategorySerialization(queryset, many=True)
       return Response(serializer.data)

class ProductCategoryCreateView(generics.CreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerialization

class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialization
    

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialization

class ProductGetbyidView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialization

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialization

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialization

#for the Contact US Serializer
class ContactGetView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerialization
    # permession = [permissions.IsAuthenticatedOrReadOnly]

class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerialization

class ContactDestroyView(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerialization