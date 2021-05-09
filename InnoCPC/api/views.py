from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse
from .decorators import is_post, is_authorized
from .models import User, UserManager
from django.shortcuts import render
from django.conf import settings
from .utils import *
from .crud import *


def login_view(request: HttpRequest):
    return render(request, 'login.html', {'BOTNAME': settings.BOTNAME})


@csrf_exempt
@is_post
def telegram_callback_login_view(request: HttpRequest):
    data = request.POST
    check_telegram_user(data)
    check_fields(request, "id")

    user = get_user_user_id(data['id'])
    if user is None:
        username = None
        if data['username'] is not None:
            username = data['username']
        user = UserManager().create_user(username=username, user_id=data['id'])
    return JsonResponse({"token": user.token})
