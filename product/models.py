from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


CATEGORY = (
    ('Labtobs','labtobs'),
    ('Food','Food'),
    ('Toys','Toys'),
    ('Phones','Phones'),
)
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    price = models.DecimalField( max_digits=7, decimal_places=2,default=0)
    category = models.CharField(max_length=50, choices=CATEGORY)
    brand = models.CharField( max_length=50)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField( default=timezone.now)
    user = models.ForeignKey(User, related_name='user_product', on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.name
