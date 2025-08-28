from django.urls import path
from .views import register, confirm, login_view


urlpatterns= [
    path('confirm/', confirm),
    path('register/', register),
    path('login_view/', login_view)

]