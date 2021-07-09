from pony.orm import Database, sql_debug

from core.settings import DEBUG

db = Database()

# if DEBUG:
#     sql_debug(True)
