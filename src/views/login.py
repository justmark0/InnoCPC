from fastapi import APIRouter, Depends, Request
from pony.orm import commit, db_session

from core.loader import templates
from core.settings import BOT_USERNAME
from models import User
from serializers.forms.user import TelegramAuthUser
from services.telegram_auth import check_telegram_user

router = APIRouter()


@router.get("/login")
def login_view(request: Request):
    context = {
        "request": request,
        "title": "InnoCPC - Login",
        "BOT_USERNAME": BOT_USERNAME,
    }
    return templates.TemplateResponse("login.html", context)


@router.post("/get_token")
@db_session
def login_view(user_data: TelegramAuthUser = Depends()):
    check_telegram_user(user_data)

    user = User.get(tg_user_id=user_data.id)
    if user is None:
        user = User(tg_user_id=user_data.id, username=user_data.username)
        commit()
    return {"token": user.token}
