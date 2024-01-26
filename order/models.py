from django.db import models
from django.contrib.auth.models import User

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
    code = models.CharField(max_length=50, default="",blank=True)
    country = models.CharField(max_length=400, default="",blank=True)
    city = models.CharField(max_length=400, default="",blank=True)
    state = models.CharField(max_length=400, default="",blank=True)
    street = models.CharField(max_length=500, default="",blank=True)
    phone_num = models.PositiveIntegerField( default=0,blank=True)
    status = models.CharField(max_length=50, choices=ORDER_STATUS,blank=True)
    total_amount = models.PositiveIntegerField( default=0,blank=True)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS,blank=True)
    payment_mode = models.CharField(max_length=400, choices=PAYMENT_MODE,blank=True)
    created_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return str(self.user)
    

class OrdersDetail(models.Model):
    order = models.ForeignKey(Orders, related_name='order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_order', on_delete=models.SET_NULL,blank=True, null=True)
    name = models.CharField( max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField( max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name
