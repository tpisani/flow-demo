from .common import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "flow.db",
    }
}

INSTALLED_APPS += (
    "django_nose",
)
