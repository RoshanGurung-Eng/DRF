from rest_framework import serializers
from .models import *

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