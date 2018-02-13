from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth import *


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the coindigo index.")


def login_user(request):
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


def submit_login(request):
    # username = request.POST.get('username')
    # password = request.POST['password']
    # print(username, password)
    # return JsonResponse({'success': False, 'error': 'Please enter both the username and password'})
    try:
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                profile_info = UserInfo.objects.get(user=user)
                return JsonResponse({'success': True, 'location': '/'})
            else:
                return JsonResponse({'success': False})
        else:
            return JsonResponse({'success': False, 'error': 'Incorrect username/password combination'})
    except:
        return JsonResponse({'success': False, 'error': 'Please enter both the username and password'})
