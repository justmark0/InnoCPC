import datetime
from datetime import datetime, timedelta

import jwt
from pony.orm import Optional, PrimaryKey, Required, Set

from core.settings import SECRET_KEY, TOKEN_EXPIRES
from models.base import db


class User(db.Entity):
    __table__ = "user"

    id = PrimaryKey(int, auto=True)
    created_at = Required(datetime, sql_default="CURRENT_TIMESTAMP")
    tg_user_id = Required(int, unique=True)  # user_id from telegram
    username = Required(str, unique=True)
    cf_username = Optional(str)
    timus_username = Optional(str)
    points = Set("Points")

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=TOKEN_EXPIRES)

        token = jwt.encode(
            {"username": self.username, "exp": int(dt.strftime("%s"))},
            SECRET_KEY,
            algorithm="HS256",
        )
        return token
