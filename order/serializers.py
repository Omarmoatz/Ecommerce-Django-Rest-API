from rest_framework import serializers

from .models import *

class OrderSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()
    class Meta:
        model = Orders
        fields = '__all__'

    def get_order_detail(self,obj):
        order = obj.order_detail.all()
        serial = OrderDetailSerializer(order,many=True).data
        return serial


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersDetail
        fields = '__all__'