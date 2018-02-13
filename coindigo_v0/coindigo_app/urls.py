from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('user/login/', views.login_user, name='login'),
    path('user/submit_login/', views.submit_login, name='submit_login'),
]