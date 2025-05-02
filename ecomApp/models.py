from django.db import models
from django.contrib.auth.models import AbstractUser
import re
from django.core.exceptions import ValidationError

# phone number validator 
def validatePhone(value):
    regex = r'^[0]{1}[7]{1}[01245678]{1}[0-9]{7}$'

    if not re.match(regex, value):
        raise ValidationError("Phone number is not valid, use this format (0710000000)")


# User model
class User(AbstractUser):
    phone = models.CharField(max_length=15, validators=[validatePhone])
    address = models.TextField()

    def __str__(self):
        return f"{self.username}, system admin - {self.is_staff}"

# Category model
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

# Product model
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    # if products is sale
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name


# Order model
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.TextField()
    phone = models.CharField(max_length=15, validators=[validatePhone])
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name
