from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter

@api_view(['GET'])
def product_list(request):
    product = Product.objects.all().order_by('id')
    filterset = ProductFilter(request.GET,product)

    paginator = PageNumberPagination()
    paginator.page_size = 5
    queryset =  paginator.paginate_queryset(filterset.qs,request)
    data = ProductSerializer(queryset,many=True).data
    return Response({
        'data':data
    })

class PostListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

@api_view(['GET'])
def product_detail(request,id):
    product = Product.objects.get(id=id)
    data = ProductSerializer(product).data
    return Response({
        'data':data,
    })