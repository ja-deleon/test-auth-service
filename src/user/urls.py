from django.urls import path
from .views import get_user, get_users, create_user, get_user_roles, get_user_permissions, login_user

#app_name='users'
urlpatterns = [
    path('users/<id>/', get_user),
    path('users/', get_users),
    path('users/<id>/roles', get_user_roles),
    path('users/<id>/permissions', get_user_permissions),
    path('signup/', create_user),
    path('login/', login_user),
]
