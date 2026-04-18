from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Chocolate
from .serializers import ChocolateSerializer

@api_view(['POST'])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
    
    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def get_chocolates(request):
    chocolates = Chocolate.objects.all()
    serializer = ChocolateSerializer(chocolates, many=True, context={'request': request})
    return Response(serializer.data)