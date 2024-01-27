from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import generics,status
from django.shortcuts import get_object_or_404
from django.db.models import Avg

from .models import Product,Review
from .serializers import ProductSerializer,ReviewSerializer
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
@permission_classes([IsAuthenticated,IsAdminUser])
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
@permission_classes([IsAuthenticated,IsAdminUser])
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

@api_view(['delete'])
@permission_classes([IsAuthenticated,IsAdminUser])
def delete_product(request,id):
    product = get_object_or_404(Product,id=id)

    if request.user != product.user:
        return Response({'detail':'sorry you can not delete this item'})
    
    product.delete()
    return Response({'detail':'you deleted this item successfully'},
                    status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request,id):
    user = request.user
    product = get_object_or_404(Product,id=id)
    data = request.data
    review = product.product_review.filter(user=user)
    
    rate = float(data['rate'])
    if rate <= 0 or rate > 10 :
        return Response({'details':'please make sure you adjust the rate between 0 and 10'})

    elif review.exists():
        new_review = {'rate':data['rate'],'content':data['content']}
        review.update(**new_review)

        ratings = product.product_review.aggregate(avg_rate=Avg('rate'))
        product.rating = ratings['avg_rate']
        product.save()
        return Response({'data':'product review updated'})
    else:
        reviews = Review.objects.create(
            user = user,
            product = product,
            rate = data['rate'],
            content = data['content']
        )
        ratings = product.product_review.aggregate(avg_rate=Avg('rate'))
        product.rating = ratings['avg_rate']
        product.save()
        serial = ReviewSerializer(reviews).data
        return Response({'data':serial})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated,IsAdminUser])
def delete_review(request,id,pk):
    product = get_object_or_404(Product,id=id)
    review = product.product_review.filter(user=request.user,id=pk)

    if review.exists():
        review.delete()
        rating = product.product_review.aggregate(avg_rate=Avg('rate'))
        if rating['avg_rate'] is None:
            rating['avg_rate'] = 0
            product.rating = rating['avg_rate']
            product.save()
            return Response({'detail':'review deleted successfully'})
        else:
            product.rating = rating['avg_rate']
            product.save()
            return Response({'detail':'review deleted successfully'})

    else:
        return Response({'detail':'there is no reviews on this product or the review id is invalid'},
                        status=status.HTTP_404_NOT_FOUND)