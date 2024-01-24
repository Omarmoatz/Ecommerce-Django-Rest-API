from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter

@api_view(['GET'])
def product_list(request):
    product = Product.objects.all().order_by('id')
    filterset = ProductFilter(request.GET,product)
    count = filterset.qs.count()

    n_page = 5
    paginator = PageNumberPagination()
    paginator.page_size = n_page
    queryset =  paginator.paginate_queryset(filterset.qs,request)
    data = ProductSerializer(queryset,many=True).data
    return Response({
        'data':data,
        'per page':n_page,
        'count':count
    })

class PostListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

@api_view(['GET'])
def product_detail(request,id):
    product = get_object_or_404(Product,id=id)
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
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_product(request,id):
    data = request.data
    product = get_object_or_404(Product,id=id)

    if request.user != product.user:
        return Response({'detail':'sorry you can not edit this item'})
    
    product.name = data['name']
    product.description = data['description']
    product.price = data['price']
    product.category = data['category']
    product.brand = data['brand']
    product.quantity = data['quantity']
    product.save()

    serializer = ProductSerializer(product).data
    return Response(serializer)

