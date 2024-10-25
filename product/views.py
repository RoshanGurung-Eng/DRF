from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializations import *
from .models import * 
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_401_UNAUTHORIZED


user = get_user_model()



# Create your views here.

# class ProductCategoryView(generics.ListAPIView):
#     queryset = ProductCategory.objects.all()
#    serializer_class = ProductCategorySerialization

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

#from rest_framework_simplejwt import RefreshToken

class LoginView(APIView):
    def post(self, request):
        email=request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request,email=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "role": user.role,
                    "email": email,
                    "refresh": str(refresh),
                    "access":str(refresh.access_token),
                    "success": "Successful login",
                 
                 },
                
            )
        else:
            return Response({"error": "Wrong credentials"}, status=HTTP_401_UNAUTHORIZED)


def home(request):
    products = Product.objects.all()  
    return render(request,'base.html', {'products': products})

class ProductCategoryView(viewsets.ViewSet):
    def list(self):
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


#For Order

class OrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerialization
    
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerialization

class OrderGetView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerialization

class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerialization

class OrderDestroyView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerialization
