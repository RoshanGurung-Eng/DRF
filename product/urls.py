from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    #users
    path("register",RegisterView.as_view(), name="register"),
    path("login",LoginView.as_view(), name="login"),
    #category CRUD
    path("category",ProductCategoryView.as_view({'get': 'list'}), name="category"),
    path("create/category",ProductCategoryCreateView.as_view(), name="category"),

    # Product list View
    path("product",ProductView.as_view(), name="product"),
    path("create/product",ProductCreateView.as_view(), name="product"),
    path("getproduct/<int:id>",ProductGetbyidView.as_view(), name="product"),
    path("updateproduct/<int:id>",ProductUpdateView.as_view(), name="product"),
    path("deleteproduct/<int:id>",ProductDeleteView.as_view(), name="product"),

    # Contact us
    path("contactus",ContactGetView.as_view(), name="contactus"),
    path("create/contactus",ContactCreateView.as_view(), name="contactus"),
    path("delete/contactus/<int:id>",ContactDestroyView.as_view(), name="contactus"),
]