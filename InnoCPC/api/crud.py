from .models import User


def get_user(username):
    return User.objects.filter(username=username).first()


def get_user_user_id(user_id):
    return User.objects.filter(user_id=user_id).first()
