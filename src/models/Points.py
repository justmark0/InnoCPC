import datetime

from pony.orm import PrimaryKey, Required

from models.base import db
from models.User import User


class Points(db.Entity):
    __table__ = "points"

    id = PrimaryKey(int, auto=True)
    user_id = Required(User)
    platform = Required(str)
    date = Required(datetime.datetime, auto=True)
    points = Required(int)
