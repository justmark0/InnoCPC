from django.shortcuts import render
from django.http import HttpRequest
from django.conf import settings


def login_view(request: HttpRequest):
    return render(request, 'login.html', {'BOTNAME': settings.BOTNAME})
