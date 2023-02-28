# -*- coding: utf-8 -*-
#                    _
#     /\            | |
#    /  \   _ __ ___| |__   ___ _ __ _   _
#   / /\ \ | '__/ __| '_ \ / _ \ '__| | | |
#  / ____ \| | | (__| | | |  __/ |  | |_| |
# /_/    \_\_|  \___|_| |_|\___|_|   \__, |
#                                     __/ |
#                                    |___/
# Copyright (C) 2017 Anand Tiwari
#
# Email:   anandtiwarics@gmail.com
# Twitter: @anandtiwarics
#
# This file is part of ArcherySec Project.

"""
Django settings for archerysecurity project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG") == "1"
# DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "SET ME")

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "archerysecurity",
    "rest_framework",
    "webscanners",
    "projects",
    "archerysettings",
    "archeryapi",
    "networkscanners",
    "staticscanners",
    'cloudscanners',
    "jiraticketing",
    "cicd",
    "tools",
    "pentest",
    "report_upload",
    "django.contrib.admin",
    "stronghold",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework.authtoken",
    "debug_toolbar",
    "dashboard",
    "background_task",
    "sitetree",
    "import_export",
    "compliance",
    "notifications",
    "user_management",
    "authentication",
    "rest_framework_simplejwt.token_blacklist",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "stronghold.middleware.LoginRequiredMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = "archerysecurity.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django_settings_export.settings_export",
                "scanners.scanner_parser.scanner_parser.parser_dict",
            ],
        },
    },
]

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

WSGI_APPLICATION = "archerysecurity.wsgi.application"

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
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

LANGUAGE_CODE = "en-us"

DEF_TIME_ZONE = "UTC"

USE_TZ = False

TIME_ZONE = os.getenv("TIME_ZONE", DEF_TIME_ZONE)

USE_I18N = True

USE_L10N = True

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

AUTH_USER_MODEL = "user_management.UserProfile"

MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

STRONGHOLD_PUBLIC_URLS = (
    r"^/admin.*?$",  # Don't touch the admin pages
    r"^/accounts/login/$",  # Avoid redirect loop
    r"^/api.*?$",
    r"^/o.*?$",
)

LOGIN_URL = "/auth/login/"

LOGIN_REDIRECT_URL = "/user/accounts/"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# SESSION_COOKIE_AGE = 5 * 100

BACKGROUND_TASK_RUN_ASYNC = True

REFRESH_TIMER = 5

SETTINGS_EXPORT = [
    "REFRESH_TIMER",
]

DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800

try:
    from archerysecurity.local_settings import *
except ImportError:
    pass

IMPORT_EXPORT_USE_TRANSACTIONS = True

# DJANGO_NOTIFICATIONS_CONFIG = {'USE_JSONFIELD': True}

DJANGO_NOTIFICATIONS_CONFIG = {"SOFT_DELETE": True}

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(levelname)s:%(name)s: %(message)s "
            "(%(asctime)s; %(filename)s:%(lineno)d)",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.StreamHandler",
        },
        "rotate_file": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "server.log",
            "encoding": "utf8",
            "maxBytes": 100000,
            "backupCount": 1,
        },
    },
    "loggers": {
        "": {"handlers": ["console", "rotate_file"], "level": "INFO"},
        "pdfminer": {"level": "CRITICAL"},
    },
}
