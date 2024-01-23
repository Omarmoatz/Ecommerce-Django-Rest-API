from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializer import SignUpSerializer,InfoSerializer


@api_view(['POST'])
def signup_api(request):
    data = request.data
    signup = SignUpSerializer(data=data)
    if signup.is_valid():
        user = User.objects.filter(username=data['email'])
        if not user.exists():
            User.objects.create(
                username = data['email'],
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
                password = make_password(data['password']),
            )
            return Response({'details':'successfully created your account'},
                            status=status.HTTP_200_OK
                    )
        else:
            return Response({'details':'this email is in use please change it'},
                            status=status.HTTP_400_BAD_REQUEST
                    )
    else:
        return Response(signup.errors)
    
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def user_info(request):
    user = InfoSerializer(request.user).data
    return Response({'data':user})
