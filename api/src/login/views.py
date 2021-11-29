from django.shortcuts import render
from rest_framework.decorators import api_view
from user.serializers import *
from rest_framework.response import Response
from rest_framework import status

#login
@api_view(['POST'])
def login_user(request):
    serializer = serializers.Serializer(data=request.data)
    if serializer.is_valid():
        data = request.data
        if User.objects.filter(username=data.get("login_name")).exists():
            user_obj = User.objects.get(username=data.get("login_name"))
            user_data = UserSerializer(user_obj).data
            login_method = "username"
            if data.get("password") == user_obj.password:
                return Response({"logged_in": True, "method": login_method, "data": user_data})
        elif User.objects.filter(email=data.get("login_name")).exists():
            user_obj = User.objects.get(email=data.get("login_name"))
            user_data = UserSerializer(user_obj).data
            login_method = "email"
            if data.get("password") == user_obj.password:
                return Response({"logged_in": True, "method": login_method, "data": user_data})
        return Response("Invalid credentials")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
