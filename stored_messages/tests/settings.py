# flake8: noqa
import django


INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.admin",
    "stored_messages",
]

try:
    import rest_framework
    INSTALLED_APPS.append("rest_framework")
except ImportError:
    pass

DEBUG = True
USE_TZ = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "stored_messages.sqlite",
    }
}

ROOT_URLCONF = "stored_messages.tests.urls"

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Django 1.10 requires the TEMPLATES settings. Deprecated since Django 1.8
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

SITE_ID = 1

MESSAGE_STORAGE = 'stored_messages.storage.PersistentStorage'

redis_host = os.environ.get("REDIS_STORED_MESSAGES_HOST", "localhost")
redis_port = os.environ.get("REDIS_STORED_MESSAGES_6379_TCP_PORT", "6379")

STORED_MESSAGES = {
    'REDIS_URL': f'redis://{redis_host}:{redis_port}/0',
}

MOCK_REDIS_SERVER = False
SECRET_KEY = 'FUUUFU'
