from django.urls import path
from .views import *

urlpatterns = [
    #for Category
    path("category",ProductCategoryView.as_view({'get': 'list'}), name="category"),
    path("create/category",ProductCategoryCreateView.as_view(), name="category"),
    #For Product
    path("product",ProductView.as_view(), name="product"),
    path("create/product",ProductCreateView.as_view(), name="product"),
    path("getproduct/<int:id>",ProductGetbyidView.as_view(), name="product"),
    path("updateproduct/<int:id>",ProductUpdateView.as_view(), name="product"),
    path("deleteproduct/<int:id>",ProductDeleteView.as_view(), name="product"),
    #for COntact
    path("contactus",ContactGetbyidView.as_view(), name="contactus"),
    path("updatecontact",ConatactUpdateView.as_view(), name="contactus"),
    path("deletecontact",ContactDeleteView.as_view(), name="contactus")

]