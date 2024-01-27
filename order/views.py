from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics,status
from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    data = request.data
    user = request.user
    order_items = data['orderItems']

    print(len(order_items))
    if len(order_items) == 0 :
        return Response({"error":"there is no items in the order"})
    
    else:
        total_amount = sum(item['price'] * item['quantity'] for item in order_items)
        order = Orders.objects.create(
            user = user,
            address = data['address'],
            phone_num = data['phone_num'],
            total_amount = total_amount,
            status = 'Shipped',
        )
        for object in order_items:
            product = get_object_or_404(Product,id=object['product_id'])
            if product.quantity < object['quantity'] :
                return Response({"error":f"there is no enough quantity from this product: {product}"})
            else:
                price = object['quantity'] * product.price
                OrdersDetail.objects.create(
                    order = order ,
                    product = product , 
                    name = product.name ,
                    quantity = object['quantity'],
                    price = price
                )
                product.quantity -= object['quantity']
                product.save()

        serial = OrderSerializer(order).data
        return Response({"data":serial})
