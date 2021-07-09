# from pony.orm import Database, sql_debug
#
# from core.settings import (POSTGRES_DB, POSTGRES_HOST, POSTGRES_PASSWORD,
#                            POSTGRES_USER, DEBUG)
#
# db = Database(
#     provider="postgres",
#     user=POSTGRES_USER,
#     password=POSTGRES_PASSWORD,
#     host=POSTGRES_HOST,
#     database=POSTGRES_DB,
# )
#
# from pony.orm import *
# import datetime
# from pony.orm.core import BindingError
#
#
# class User(db.Entity):
#     __table__ = "user"
#
#     id = PrimaryKey(int, auto=True)
#     created_at = Required(datetime.datetime, auto=True)
#     tg_user_id = Required(int, unique=True)  # user_id from telegram
#     username = Required(str, unique=True)
#     cf_username = Optional(str)
#     timus_username = Optional(str)
#     points = Set('Points')
#
#
# class Points(db.Entity):
#     __table__ = "points"
#
#     id = PrimaryKey(int, auto=True)
#     user_id = Required(User)
#     platform = Required(str)
#     date = Required(datetime.datetime, auto=True)
#     points = Required(int)
#
# try:
#     db.generate_mapping(create_tables=True)
# except BindingError:
#     pass
#
# if DEBUG:
#     sql_debug(True)
