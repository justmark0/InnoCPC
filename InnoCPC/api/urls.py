from django.urls import path
from .views import *

urlpatterns = [
    path('login', login_view),  # move to backend
    path('get_token', get_token_view),
]
