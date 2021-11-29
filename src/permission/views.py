from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from .models import *

@api_view(['GET', 'POST'])
def get_permissions(request):
    if request.method == 'GET':
        permissions_obj = Permission.objects.all()
        permissions_data = PermissionSerializer(permissions_obj, many=True).data
        return Response({"permissions": permissions_data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PermissionSerializer(data=request.data)
        if serializer.is_valid():
            Permission.objects.create(**serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
