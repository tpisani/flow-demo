from .common import *

import dj_database_url


DEBUG = False

ALLOWED_HOSTS = ["*"]

db_config = dj_database_url.config(env="CLEARDB_DATABASE_URL")
db_config.pop("OPTIONS", None)

DATABASES["default"] = db_config
