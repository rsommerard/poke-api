from .base import *  # noqa: F401, F403

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS += ["django_extensions"]  # noqa: F405
