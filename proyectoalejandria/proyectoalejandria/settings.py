from email.utils import getaddresses
from pathlib import Path
from typing import cast

from environ import Env


env = Env()
env.read_env(".env")
env.read_env(".env.defaults")


# Application definition

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = cast(bool, env.bool("DEBUG"))

APP_URL = cast(str, env.str("APP_URL"))

ALLOWED_HOSTS = cast(list, env.list("ALLOWED_HOSTS"))
ALLOWED_HOSTS.append(APP_URL)

SITE_ID = 1


INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # 3rd party
    "rest_framework",
    "djoser",
    "rest_framework_simplejwt.token_blacklist",
    # 1st party
    "users",
    "main",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "proyectoalejandria.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "proyectoalejandria.wsgi.application"


# Database

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DATABASES = {
    "default": env.db("DB_URL"),
}


# Security

AUTH_PASSWORD_VALIDATORS = []

if not DEBUG:
    AUTH_PASSWORD_VALIDATORS.extend(
        [
            {
                "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
            },
            {
                "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
            },
            {
                "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
            },
            {
                "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
            },
        ]
    )

AUTH_USER_MODEL = "users.User"

CSRF_COOKIE_SECURE = env.bool("USE_HTTPS", default=False)

SESSION_COOKIE_SECURE = env.bool("USE_HTTPS", default=False)

if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOWED_ORIGINS = [
        APP_URL,
    ]


# Communication

ADMINS = getaddresses(cast(list, env.list("ADMINS", default=[])))

DEFAULT_FROM_EMAIL = env.str(
    "DEFAULT_FROM_EMAIL",
    default="Proyecto Alejandría <info@proyectoalejandria.org>",
)

if not DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

    EMAIL_USE_SSL = env.bool("EMAIL_USE_SSL", default=True)

    DEFAULT_FROM_EMAIL = env.str("EMAIL_FROM")
    SERVER_EMAIL = DEFAULT_FROM_EMAIL

    EMAIL_CONFIG = env.email_url("EMAIL_URL")
    vars().update(EMAIL_CONFIG)
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Internationalization

LANGUAGE_CODE = "es-es"

TIME_ZONE = "Europe/Madrid"

USE_I18N = True

USE_TZ = True


# Static files

STATIC_URL = "static/"


# App public settings

REGISTER_ENABLED = cast(bool, env.bool("REGISTER_ENABLED"))

PUBLIC_SITE = cast(bool, env.bool("PUBLIC_SITE"))


# Rest Framework

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "60/minute",
    },
}

if DEBUG:
    cast(list, REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"]).append(
        "rest_framework.renderers.BrowsableAPIRenderer"
    )

    cast(list, REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"]).append(
        # To allow authentication in the browsable API
        "rest_framework.authentication.SessionAuthentication"
    )

DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "cuenta/reiniciar-clave/{uid}/{token}",
    "ACTIVATION_URL": "cuenta/activar/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "PERMISSIONS": {
        "username_reset": ["rest_framework.permissions.IsAdminUser"],
        "username_reset_confirm": ["rest_framework.permissions.IsAdminUser"],
        "set_username": ["rest_framework.permissions.IsAdminUser"],
        "user_delete": ["rest_framework.permissions.IsAdminUser"],
    },
    "SERIALIZERS": {
        "current_user": "users.serializers.CurrentUserSerializer",
        "user_create": "users.serializers.CreateUserSerializer",
    },
}

if not REGISTER_ENABLED:
    DJOSER["PERMISSIONS"]["user_create"] = ["rest_framework.permissions.IsAdminUser"]

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ROTATE_REFRESH_TOKENS": True,
}

if not DEBUG:
    SIMPLE_JWT["BLACKLIST_AFTER_ROTATION"] = True
