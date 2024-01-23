from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product(request):
    data = request.data
    add_form = ProductSerializer(data=data)
    if add_form.is_valid():
        product = Product.objects.create(**data, user=request.user)
        pdct = ProductSerializer(product).data
        return Response({'data':pdct})
    else:
        return Response(add_form.errors)