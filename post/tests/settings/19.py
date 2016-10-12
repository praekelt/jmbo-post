import os
from os.path import expanduser


USE_TZ = True

TIME_ZONE = "Africa/Johannesburg"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "jmbo",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

INSTALLED_APPS = (
    "post",
    "jmbo",
    "photologue",
    "category",
    "ckeditor",
    "django_comments",
    "likes",
    "secretballot",
    "pagination",
    "preferences",
    "ultracache",
    "sites_groups",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
)

ROOT_URLCONF = "post.tests.urls"

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "likes.middleware.SecretBallotUserIpUseragentMiddleware",
    "pagination.middleware.PaginationMiddleware",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.template.context_processors.debug",
    "django.template.context_processors.i18n",
    "django.template.context_processors.media",
    "django.template.context_processors.static",
    "django.template.context_processors.tz",
    "django.template.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.realpath(os.path.dirname(__file__)) + "/../templates/",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": TEMPLATE_CONTEXT_PROCESSORS,
        },
    },
]

SITE_ID = 1

STATIC_URL = "/static/"

# Disable celery
CELERY_ALWAYS_EAGER = True
BROKER_BACKEND = "memory"

SECRET_KEY = "SECRET_KEY"

DEBUG = True

# Ultracache triggers lazy creation of content types. This prevents that code
# path.
ULTRACACHE = {"invalidate": False}

CKEDITOR_UPLOAD_PATH = expanduser("~")

REST_FRAMEWORK = {
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning"
}
