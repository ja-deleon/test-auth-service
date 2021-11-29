from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from .models import *
from django.db import IntegrityError

@api_view(['GET', 'POST'])
def get_roles(request):
    if request.method == 'GET':
        roles_obj = Role.objects.all()
        roles_data = RoleSerializer(roles_obj, many=True).data
        return Response({"roles": roles_data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError:
                data = serializer.data
                if Role.objects.filter(id=data.get("id")).exists():
                    return Response("duplicate id")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def update_role(request):
#     serializer = RoleSerializer(data=request.data)
#     if serializer.is_valid():
#         try:
#             serializer.save()
#         except IntegrityError:
#             data = serializer.data
#             if Role.objects.filter(id=data.get("id")).exists():
#                 return Response("duplicate id")
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
