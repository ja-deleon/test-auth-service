from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from .models import *
from .forms import *
from role.models import Role
from role.serializers import *
from permission.models import Permission
from permission.serializers import *
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

#retrieve all users
@api_view(['GET'])
def get_users(request):
    users_obj = User.objects.all()
    users_data = UserSerializer(users_obj, many=True).data
    return Response({"data": users_data}, status=status.HTTP_200_OK)

#retrieve specific user
@api_view(['GET'])
def get_user(request, id):
    try:
        user_data = get_user_data(id)
        return Response({"data": user_data}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        raise IndexError("Index out of bounds")

# #sign up
# @api_view(['POST'])
# def create_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         try:
#             serializer.save()
#         except IntegrityError:
#             data = serializer.data
#             if User.objects.filter(username=data.get("username")).exists():
#                 return Response("username already taken")
#             elif User.objects.filter(email=data.get("email")).exists():
#                 return Response("email already in use")
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # login
# @api_view(['POST'])
# def login_user(request):
#     serializer = serializers.Serializer(data=request.data)
#     if serializer.is_valid():
#         data = request.data
#         if User.objects.filter(username=data.get("login_name")).exists():
#             user_obj = User.objects.get(username=data.get("login_name"))
#             user_data = UserSerializer(user_obj).data
#             login_method = "username"
#             if data.get("password") == user_obj.password:
#                 return Response({"logged_in": True, "method": login_method})
#         elif User.objects.filter(email=data.get("login_name")).exists():
#             user_obj = User.objects.get(email=data.get("login_name"))
#             user_data = UserSerializer(user_obj).data
#             login_method = "email"
#             if data.get("password") == user_obj.password:
#                 return Response({"logged_in": True, "method": login_method, "data": user_data})
#         return Response("Invalid credentials")
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#modify user
@api_view(['POST'])
def update_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.data
        if User.objects.filter(username=data.get("username")).exists():
            instance = User.objects.get(username=data.get("username"))
        elif User.objects.filter(email=data.get("email")).exists():
            instance = User.objects.get(email=data.get("email"))
        serializer.update(instance, data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_user_roles(request, id):
    if request.method == 'GET':
        user_data = get_user_data(id)
        role_data = get_role_data(user_data)
        return Response({"data": user_data, "roles": role_data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            instance = User.objects.get(id=id)
            serializer.update(instance, data)
            role_data = get_role_data(serializer.data)
            return Response({"data":serializer.data, "roles": role_data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_user_permissions(request, id):
    user_data = get_user_data(id)
    roles_data = get_role_data(user_data)
    permissions_data = get_permissions_data(roles_data)
    if request.method == 'GET':
        # user_data = get_user_data(id)
        # roles_data = get_role_data(user_data)
        # permissions_data = get_permissions_data(roles_data)
        return Response({"data": user_data, "permissions": permissions_data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = serializers.Serializer(data=request.data)
        if serializer.is_valid():
            data = request.data
            without_permissions = []
            with_permissions = []
            no_such_permission = []
            ids_list = data.get("ids")
            ids = ids_list.split(",")
            for permission_id in ids:
                try:
                    permission_obj = Permission.objects.get(id=permission_id)
                    permission_data = PermissionSerializer(permission_obj).data
                    if permission_data in permissions_data:
                        with_permissions.append(permission_data)
                    else:
                        without_permissions.append(permission_data)
                except ObjectDoesNotExist:
                    no_such_permission.append({"id": permission_id})


            return Response({"data": user_data, "with_permissions": with_permissions, "without_permissions": without_permissions, "no_such_permission": no_such_permission}, status=status.HTTP_200_OK)
        else:
            return Response("Invalid request")



#utilities
def get_user_data(id):
    user_obj = User.objects.get(id=id)
    user_data = UserSerializer(user_obj).data
    return user_data

def get_role_data(user_data):
    role_ids = user_data.get("role_id")
    role_ids_list = role_ids.split(",")
    roles_data = []
    for role_id in role_ids_list:
        role_obj = Role.objects.get(id=role_id)
        role_data = RoleSerializer(role_obj).data
        roles_data.append(role_data)
    return roles_data

def get_permissions_data(roles_data):
    for role_data in roles_data:
        permissions_ids = role_data.get("permissions")
        permissions_ids_list = permissions_ids.split(",")
        permissions_data = []

        for permission_id in permissions_ids_list:
            permission_obj = Permission.objects.get(id=permission_id)
            permission_data = PermissionSerializer(permission_obj).data
            permissions_data.append(permission_data)
    return permissions_data

