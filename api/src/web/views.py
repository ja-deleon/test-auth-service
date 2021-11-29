from django.shortcuts import render
from django.http import HttpResponse
import requests
from user.models import User
from user.serializers import *

login_url = "http://127.0.0.1:8000/api/login/"
signup_url = "http://127.0.0.1:8000/api/signup/"
users_url = "http://127.0.0.1:8000/api/users/"
roles_url = "http://127.0.0.1:8000/api/roles/"
permissions_url = "http://127.0.0.1:8000/api/permissions/"
headers = {'Content-type': 'application/json'}

def home_view(request):
    #return HttpResponse("<h1>home_view</h1>")
    return render(request, "home.html", {})

def login_view(request):
    #return HttpResponse("<h1>login_view</h1>")
    return render(request, "login.html", {})

def login(request):
    response = requests.post(login_url, json=request.POST, headers=headers)
    login_data = response.json()
    context = {
        "obj": login_data
    }
    return render(request, "dashboard.html", context)

def signup_view(request):
    #return HttpResponse("<h1>login_view</h1>")
    return render(request, "signup.html", {})

def signup(request):
    response = requests.post(signup_url, json=request.POST, headers=headers)
    signup_data = response.json()
    context = {
        "obj": signup_data
    }
    return render(request, "dashboard.html", context)

def users_view(request):
    response = requests.get(users_url)
    users_data = response.json()
    context = {
        "obj": users_data
    }
    return render(request, "users_dashboard.html", context)

def roles_view(request):
    response = requests.get(roles_url)
    roles_data = response.json()
    context = {
        "obj": roles_data
    }
    return render(request, "roles_dashboard.html", context)

def create_role(request):
    response = requests.post(roles_url, json=request.POST, headers=headers)
    response_data = response.json()
    context = {
        "obj": response_data
    }
    return render(request, "create_role.html", context)

def create_role_view(request):
    return render(request, "create_role.html", {})

def permissions_view(request):
    response = requests.get(permissions_url)
    permissions_data = response.json()
    context = {
        "obj": permissions_data
    }
    return render(request, "permissions_dashboard.html", context)

def create_permission(request):
    response = requests.post(permissions_url, json=request.POST, headers=headers)
    response_data = response.json()
    context = {
        "obj": response_data
    }
    return render(request, "create_permission.html", context)

def create_permission_view(request):
    return render(request, "create_permission.html", {})

def view_role(request):
    response = requests.get(users_url+request.GET.get("id")+"/roles")
    role_data = response.json()
    context = {
        "obj": role_data
    }
    return render(request, "roles_dashboard.html", context)

def add_role_view(request):
    user_obj = User.objects.get(id=request.GET.get("id"))
    context = {
        "obj": user_obj
    }
    return render(request, "add_user_role.html", context)


def add_role(request):
    url = users_url + request.POST.get("id") + "/roles"
    response = requests.post(url, json=request.POST, headers=headers)
    user_role_data = response.json()
    context = {
        "obj": user_role_data
    }
    return render(request, "add_user_role.html", context)