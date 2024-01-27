from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from product.models import Product

ORDER_STATUS = (
    ('Processing','Processing'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)
PAYMENT_STATUS = (
    ('Paid','Paid'),
    ('Unpaid','Unpaid'),
)
PAYMENT_MODE = (
    ('COD','COD'),
    ('Card','Card'),
)

class Orders(models.Model):
    user = models.ForeignKey(User, related_name='user_order', on_delete=models.CASCADE)
    code = models.CharField(max_length=50, default=get_random_string(10),blank=True)
    address = models.TextField(max_length=1000, help_text= 'please enter these data (country, city, state, street)',default="",blank=True)
    phone_num = models.CharField(max_length=100, default="",blank=True)
    status = models.CharField(max_length=50, choices=ORDER_STATUS,default='Processing',blank=True)
    total_amount = models.PositiveIntegerField( default=0,blank=True)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS,default='Unpaid',blank=True)
    payment_mode = models.CharField(max_length=400, choices=PAYMENT_MODE,default='COD',blank=True)
    created_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return str(self.user)
    

class OrdersDetail(models.Model):
    order = models.ForeignKey(Orders, related_name='order_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_order', on_delete=models.SET_NULL,blank=True, null=True)
    name = models.CharField( max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField( max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name
