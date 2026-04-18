from django.urls import path
from .views import get_chocolates, login_user

urlpatterns = [
    path('chocolates/', get_chocolates),
    path('login/', login_user),
]