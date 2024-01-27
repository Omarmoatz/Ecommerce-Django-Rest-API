from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import generics,status
from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_list(request):
    order = Orders.objects.all()
    serializer = OrderSerializer(order, many=True).data
    return Response({'data':serializer},
                    status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_detail(request,id):
    order = get_object_or_404(Orders,id=id)
    serializer = OrderSerializer(order).data
    return Response({'data':serializer},
                    status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsAdminUser])
def update_order(request,id):
    data = request.data
    user = request.user
    order = get_object_or_404(Orders,id=id)

    if user != order.user:
        return Response({"error":'you can not updete this order'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    order.address = data['address']
    order.phone_num = data['phone_num']
    order.status = data['status']
    order.payment_mode = data['payment_mode']
    order.save()
    
    serializer = OrderSerializer(order).data
    return Response({'data':serializer},
                    status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated,IsAdminUser])
def delete_order(request,id):
    order = get_object_or_404(Orders,id=id)

    if request.user != order.user:
        return Response({"error":'you can not delete this order'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    order.delete()
    return Response({'data':'deleted successfully'},
                    status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    data = request.data
    user = request.user
    order_items = data['orderItems']

    print(len(order_items))
    if len(order_items) == 0 :
        return Response({"error":"there is no items in the order"},
                        status=status.HTTP_404_NOT_FOUND)
    
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
                return Response({"error":f"there is no enough quantity from this product: {product}"},
                                status=status.HTTP_404_NOT_FOUND)
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
        return Response({"data":serial},
                        status=status.HTTP_200_OK)
