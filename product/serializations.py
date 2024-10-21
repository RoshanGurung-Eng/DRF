from rest_framework import serializers
from .models import *

class ProductCategorySerialization(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ["id", "category_name", "category_img"]


class ProductSerialization(serializers.ModelSerializer):
    category =ProductCategorySerialization(read_only= True)
    class Meta:
        model = Product
        fields = "__all__"
