from .response import invalid_request_params


def check_fields(request, *fields):
    for field in fields:
        if field not in request.POST.keys():
            return invalid_request_params()
    return None
