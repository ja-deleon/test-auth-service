from django.urls import path
from .views import get_roles

urlpatterns = [
    path('roles/', get_roles),
]
