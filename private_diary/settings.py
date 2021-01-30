"""
Django settings for private_diary project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from django.contrib.messages import constants as messages
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd$dp$&432y@9d=5@i3k_*-cd_&*-rhixpi5f-%nq4tz8++il%m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'diary.apps.DiaryConfig',
    'accounts.apps.AccountsConfig',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
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

ROOT_URLCONF = 'private_diary.urls'

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

WSGI_APPLICATION = 'private_diary.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'private_diary',
        'USER': '',
        'PASSWORD': '',
        # 'USER': os.environ.get('DB_USER'),
        # 'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': '',
        'POST': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_URL = '/static/'


#ロギング設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    #ロガーの設定
    'loggers':{
        #Djangoが利用するロガー
        'django':{
            'handlers': ['console'],
            'level': 'INFO',
        },
    #diaryアプリケーションが利用するロガー
    'diary':{
        'handlers': ['console'],
        'level': 'DEBUG',
        },
    },
    #ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev',
        },
    },
    #フォーマッタの設定
    'formatters':{
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s',
            ])
        },
    }
}


MESSAGE_TAGS = {
    messages.ERROR: 'alert alert-danger',
    messages.WARNING: 'alert alert-warning',
    messages.SUCCESS: 'alert alert-success',
    messages.INFO: 'alert alert-info',
}

AUTH_USER_MODEL = 'accounts.CustomUser'

# #django-allauthで利用するdjango.contrib.sitesを使うためにサイト識別用IDを設定
SITE_ID = 1

AUTHENTICATION_BAKCENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    #一般ユーザー用(メールアドレス認証)
    'django.contrib.auth.backends.ModelBackend',
    #管理サイト用(ユーザー名認証)
)

#メールアドレス認証に変更する設定
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False

#サインアップにめーるアドレス確認をはさむよう設定
ACCOUNT_EMAIL_VERFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True

#ログイン/ログアウト後の遷移先を設定
LOGIN_REDIRECT_URL = 'diary:diary_list'
ACCOUNT_LOGOUT_REDIRECT = 'account_login'

#ログアウトクリックのクリック一発でログアウトする設定
ACCOUNT_LOGOUT_ON_SET = True

#django-allauthが送信するメールの件名に自動付与される接頭辞をブランクにする設定
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''

#デフォルトのメール設定元を設定
DEFAULT_FROM_EMAIL = 'admin@exmaple.com'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'