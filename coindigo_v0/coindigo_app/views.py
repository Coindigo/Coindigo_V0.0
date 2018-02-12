from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import *


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the coindigo index.")


def login(request):
    current_profile_info = request.user
    if not current_profile_info.is_anonymous:
        current_profile_info = UserInfo.objects.get(user=current_profile_info)
    else:
        current_profile_info = None
    context = {
        'title': 'Coindigo - Login',
        'current_profile_info': current_profile_info,
    }
    return render(request, 'login.html', context)