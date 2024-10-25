from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Permission, Group
from core import settings

user = settings.AUTH_USER_MODEL
# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
  
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.IntegerField(default=0)

    groups = models.ManyToManyField(
        Group,
        related_name='charging_user_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        verbose_name=('groups'),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='charging_user_set',
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user_permissions'),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email



class ProductCategory(models.Model):
    category_name = models.CharField(max_length=255)  
    category_img = models.ImageField(upload_to="category/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category_name} and {self.created_at}"
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()   
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=True)
    product_img = models.ImageField(upload_to="product/", null=True, blank=True)
    stock = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} and {self.category}"
    
class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField(default= 0)
    email = models.EmailField()
    message = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    orderStatus = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"self.user.username"