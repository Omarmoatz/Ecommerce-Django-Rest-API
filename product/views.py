from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def product_list(request):
    product = Product.objects.all()
    data = ProductSerializer(product,many=True).data
    return Response({
        'data':data
    })
