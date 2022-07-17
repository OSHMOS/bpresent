"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
import json
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# screts.json 파일 위치를 명시
secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting):
    '''비밀 변수를 가져오거나 명시적 예외를 반환한다.'''
    try:
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret('SECRET_KEY')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '.ap-northeast-2.compute.amazonaws.com',
    '127.0.0.1',
    '.bpresent.kr'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.sites",
    'attendance',
    'common',
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    'bootstrap5',
    'fontawesomefree',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# aws rds - postgresql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'bpresent',
#         'USER': 'postgres',
#         'PASSWORD': 'ksaet0729$',
#         'HOST': 'database-2.ckg7dajjkqpk.ap-northeast-2.rds.amazonaws.com',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auth settings
AUTH_USER_MODEL = "common.User"

LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'card_list'
LOGOUT_REDIRECT_URL = 'index'

ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

# 임시로 이메일 인증을 어떻게 보낼지 설정해줍니다.
# 현재는 콘솔을 통해서 이메일을 보낸다고 설정할 겁니다.
# Email settings

# 사이트와 관련한 자동응답을 받을 이메일 주소
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# 메일을 호스트하는 서버
EMAIL_HOST = 'smtp.naver.com'

# naver e-mail과의 통신하는 포트
EMAIL_PORT = '465'

# 발신할 이메일
EMAIL_HOST_USER = 'ojames97@naver.com'

# 발신할 메일의 비밀번호
smtp_password_file = os.path.join(BASE_DIR, 'smtp_password.json')

with open(smtp_password_file) as f:
    smtp_password = json.loads(f.read())


def get_secret(setting):
    '''비밀 변수를 가져오거나 명시적 예외를 반환한다.'''
    try:
        return smtp_password[setting]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)


EMAIL_HOST_PASSWORD = get_secret('EMAIL_HOST_PASSWORD')

# SSL 보안 방법
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
