import hashlib
import hmac
from time import time

from fastapi import HTTPException

from core.settings import BOT_TOKEN
from serializers.forms.user import TelegramAuthUser


def check_telegram_user(data: TelegramAuthUser):
    if time() - data.auth_date > 86400:
        raise HTTPException(status_code=400, detail="Outdated time")

    user_data = f"auth_date={data.auth_date}\nfirst_name={data.first_name}\nid={data.id}\nusername={data.username}"
    token_sha = hashlib.sha256(BOT_TOKEN.encode("utf-8")).digest()
    signature = hmac.new(
        key=token_sha, msg=bytes(user_data, "utf-8"), digestmod=hashlib.sha256
    ).hexdigest()

    if signature != data.hash:
        return HTTPException(status_code=400, detail="Invalid hash")
