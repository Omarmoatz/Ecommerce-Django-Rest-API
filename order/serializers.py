from rest_framework import serializers

from .models import *

class OrderSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField(method_name='order_details')
    class Meta:
        model = Orders
        fields = '__all__'

    def order_details(self,obj):
        order = obj.order_detail.all()
        serial = OrderDetailSerializer(order,many=True).data
        return serial


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersDetail
        fields = '__all__'