from django.http import JsonResponse


def invalid_request_params():
    return JsonResponse({
        'ok': False,
        'error_code': 401,
        })


def database_existence_error():
    return JsonResponse({
        'ok': False,
        'error_code': 402,
        })


def unauthorized_request():
    return JsonResponse({
        'ok': False,
        'error_code': 403,
        })


def invalid_request_method():
    return JsonResponse({
        'ok': False,
        'error_code': 404,
        })
