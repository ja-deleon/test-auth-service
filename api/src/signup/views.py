from django.shortcuts import render
from rest_framework.decorators import api_view
from user.serializers import *
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status

#sign up
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
        except IntegrityError:
            data = serializer.data
            if User.objects.filter(username=data.get("username")).exists():
                return Response("username already taken")
            elif User.objects.filter(email=data.get("email")).exists():
                return Response("email already in use")

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
