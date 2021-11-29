from django.urls import path
from .views import home_view, login_view, login, signup_view, signup, users_view, roles_view, permissions_view, create_role_view, create_permission_view, create_role, create_permission, view_role, add_role, add_role_view

urlpatterns = [
    path('', home_view),
    path('login/', login_view),
    path('signup/', signup_view),
    path('login_action/', login),
    path('signup_action/', signup),
    path('users/', users_view),
    path('roles/', roles_view),
    path('create_role/', create_role),
    path('create_role_view/', create_role_view),
    path('permissions/', permissions_view),
    path('create_permission/', create_permission),
    path('create_permission_view/', create_permission_view),
    path('view_role', view_role),
    path('add_role/', add_role),
    path('add_role_view', add_role_view),
]