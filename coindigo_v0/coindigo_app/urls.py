from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('user/login', views.login, name='login'),
]