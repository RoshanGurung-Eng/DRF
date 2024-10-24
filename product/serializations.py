from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id','username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validated_data):
            user = user.objects.create_user(
                username =validated_data['username'],
                email = validated_data['email'],
                password = validated_data['password'] 
            )


class ProductCategorySerialization(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        # fields = "_all_"
        fields = ['id', 'category_name','category_img']
        
class ProductSerialization(serializers.ModelSerializer):
    category = ProductCategorySerialization(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title','description','product_img','stock',
        'price','category']

class ContactSerialization(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'phone', 'email']

class CustomUserSerialization(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username', ' email', ]