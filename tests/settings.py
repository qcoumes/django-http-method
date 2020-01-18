import django

DEBUG = True

SECRET_KEY = 'TERCES'

INSTALLED_APPS = [
    'django_http_method',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
]

# Templates engines
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

MIDDLEWARE = MIDDLEWARE_CLASSES = []

ROOT_URLCONF = 'tests.urls'

# Database
DATABASES = {}

# Allow test without database
TEST_RUNNER = 'tests.testing.DatabaselessTestRunner'
