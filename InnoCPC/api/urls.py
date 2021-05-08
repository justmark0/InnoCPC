from django.urls import path
from .views import *

urlpatterns = [
    path('login', login_view),  # move to backend
    path('get_token', telegram_callback_login_view),
]
