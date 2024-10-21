from django.urls import path
from .views import *

urlpatterns = [
    path("category",ProductCategoryView.as_view(), name="productcategory-list"),
    path("create/category",ProductCreateCategoryView.as_view(), name="productcategory-create"),
    path("product",ProductView.as_view(), name="product-list"),
    path("create/product",ProductCreateView.as_view(), name="product-create"),
    path("product",ProductView.as_view(), name="product-list"),
    path("product",ProductView.as_view(), name="product-list"),
    
]