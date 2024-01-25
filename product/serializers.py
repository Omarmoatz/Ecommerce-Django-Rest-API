from rest_framework import serializers
from .models import Product,Review


class ProductSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(method_name='get_review')

    class Meta:
        model = Product
        fields = '__all__'

    def get_review(self,obj):
        review = obj.product_review.all()
        serial = ReviewSerializer(review ,many=True).data
        return serial

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'