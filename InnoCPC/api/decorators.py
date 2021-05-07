from django.conf import settings
from .crud import get_user
from .response import *
import jwt


# Checks that the request is authorized
def is_authorized(view):
    def check_token(request):
        if 'token' not in request.POST:
            return invalid_request_params()

        # Check that the request is authorized
        user_data = jwt.decode(request.POST['token'], settings.SECRET_KEY, algorithm='HS256')
        if 'username' not in user_data.keys():
            return invalid_request_params()
        user = get_user(request.POST['username'])
        if not user:
            return unauthorized_request()
        return view(request, user)

    return check_token


# Checks that the request method is POST
def is_post(view):
    def check_request(request):
        if request.method != 'POST':
            return invalid_request_method()
        return view(request)

    return check_request
