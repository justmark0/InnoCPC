from .response import invalid_request_params
from django.conf import settings
import hashlib
import hmac
import time


def check_fields(request, *fields):
    for field in fields:
        if field not in request.POST.keys():
            return invalid_request_params()


def check_telegram_user(data):
    sha_list = []
    if not data['auth_date'].isnumeric:
        return invalid_request_params()

    if int(time.time()) - int(data['auth_date']) > 86400:
        return invalid_request_params()
    keys = sorted(data.keys())
    for key in keys:
        # if key in ['auth_date', 'first_name', 'id', 'username']:
        if key != 'hash':
            sha_list.append(f'{key}={data[key]}')

    user_data = bytes('\n'.join(sha_list), 'utf-8')
    token_sha = hashlib.sha256(settings.BOTTOKEN.encode('utf-8')).digest()
    signature = hmac.new(key=token_sha, msg=user_data, digestmod=hashlib.sha256).hexdigest()

    if signature != data['hash']:
        return invalid_request_params()

