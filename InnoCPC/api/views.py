from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse
from .decorators import is_post, is_authorized
from .response import invalid_request_params
from .models import User, UserManager
from django.shortcuts import render
from django.conf import settings
from .utils import check_fields
from .crud import *
import hashlib


def login_view(request: HttpRequest):
    return render(request, 'login.html', {'BOTNAME': settings.BOTNAME})


@is_post
@csrf_exempt
def telegram_callback_login_view(request: HttpRequest):
    sha_list = []
    data = request.POST
    for key in data.keys():
        sha_list.append(f'{key}={data[key]}')
    sha_list.sort()
    sha_str = hashlib.sha256("\n".join(sha_list)).hexdigest()
    if sha_str != data['hash']:
        return invalid_request_params()

    if error := check_fields(request, "user_id") is not None:
        return error
    user = get_user_user_id(data['user_id'])
    if user is None:
        user = UserManager().create_user("username", user_id=data['user_id'])
    return JsonResponse({"token": user.token})
