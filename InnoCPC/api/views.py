from django.shortcuts import render
from django.http import HttpRequest
from django.conf import settings
from .decorators import is_post, is_authorized
from .models import User

@is_post
@is_authorized
def login_view(request: HttpRequest, user: User):
    return render(request, 'login.html', {'BOTNAME': settings.BOTNAME})
