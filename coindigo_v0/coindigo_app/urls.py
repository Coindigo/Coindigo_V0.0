from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('user/login/', views.login_user, name='login'),
    path('user/submit_login/', views.submit_login, name='submit_login'),
    path('user/dashboard/<int:user_id>', views.dashboard, name='dashboard'),
    path('user/dashboard/edit/<int:user_id>/', views.user_edit, name='user_edit'),
]