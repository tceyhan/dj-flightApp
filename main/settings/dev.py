from .base  import *

THIRD_PARTY_APPS = [
     "debug_toolbar",
]

INSTALLED_APPS += THIRD_PARTY_APPS

THIRD_PARTY_MIDDLEWARE = [
     #! debug toolbar için
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

MIDDLEWARE += THIRD_PARTY_MIDDLEWARE

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'locale-db.sqlite3',
    }
}

#! debug toolbar için
INTERNAL_IPS = [ 
    "127.0.0.1" 
]

# https://docs.djangoproject.com/en/4.0/topics/logging/

LOGGING = {
    "version": 1,
    # is set to True then all loggers from the default configuration will be disabled.
    "disable_existing_loggers": True,
    # Formatters describe the exact format of that text of a log record. 
    "formatters": {
        "standard": {
            "format": "[%(levelname)s] %(asctime)s %(name)s: %(message)s"
        },
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    # The handler is the engine that determines what happens to each message in a logger.
    # It describes a particular logging behavior, such as writing a message to the screen, 
    # to a file, or to a network socket.
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "WARNING",
            "stream": "ext://sys.stdout",
            },
        'file': {
            'class': 'logging.FileHandler',
            "formatter": "verbose",
            'filename': './debug.log',
            'level': 'WARNING',
        },
    },
    # A logger is the entry point into the logging system.
    "loggers": {
        "django": {
            "handlers": ["console", 'file'],
            # log level describes the severity of the messages that the logger will handle. 
            "level": config("DJANGO_LOG_LEVEL"),
            'propagate': True,
            # If False, this means that log messages written to django.request 
            # will not be handled by the django logger.
        },
    },
}
