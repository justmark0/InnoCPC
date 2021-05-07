from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse
from .decorators import is_post, is_authorized
from django.shortcuts import render
from django.conf import settings
from .utils import check_fields
from .crud import *
from .models import User, UserManager


def login_view(request: HttpRequest):
    return render(request, 'login.html', {'BOTNAME': settings.BOTNAME})


@is_post
@csrf_exempt
def get_token_view(request: HttpRequest):
    if error := check_fields(request, "username", "user_id") is not None:
        return error
    data = request.POST
    user = get_user_user_id(data['user_id'])
    if user is None:
        user = UserManager().create_user("username", user_id=data['user_id'])
    return JsonResponse({"token": user.token})
