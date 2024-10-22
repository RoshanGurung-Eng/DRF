from django.db import models

# Create your models here.

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
