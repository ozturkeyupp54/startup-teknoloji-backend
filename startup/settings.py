import os
import datetime
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("DJANGO_SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID = 1
# CMS_CONFIRM_VERSION4 = True

INSTALLED_APPS = [
    'multi_captcha_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',    
    
    # Modules:
    # 'rest_framework',
    'rest_framework_simplejwt',
    # 'django_filters',
    # 'corsheaders',
    'django_ckeditor_5',
    'import_export',
    'crispy_forms',
    'crispy_bootstrap5',  
    
    # Apps:

    'anket.apps.AnketConfig',
    'alt_reklam_alani.apps.AltReklamAlaniConfig',
    'advertisement.apps.AdvertisementConfig',
    'investor.apps.InvestorConfig',
    'girisimci.apps.GirisimciConfig',
    'girisim.apps.GirisimConfig',
    'author.apps.AuthorConfig',
    'post.apps.PostConfig',
    'user.apps.UserConfig',
    'category.apps.CategoryConfig',
    'comment.apps.CommentConfig',
    'authentication.apps.AuthenticationConfig',
    'sitesettings.apps.SitesettingsConfig',
    
    # 'cms',
    # 'menus',
    # 'treebeard',
    # 'django_check_seo',
    'meta',
    'captcha',

]

MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

MIDDLEWARE = [
    # 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

ROOT_URLCONF = 'startup.urls'

ALLOWED_HOSTS = ['*']

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

WSGI_APPLICATION = 'startup.wsgi.application'

AUTH_USER_MODEL = 'user.User'

ACCESS_TOKEN_LIFETIME = datetime.timedelta(hours=2)
REFRESH_TOKEN_LIFETIME = datetime.timedelta(days=1)

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': ACCESS_TOKEN_LIFETIME,
    'REFRESH_TOKEN_LIFETIME': REFRESH_TOKEN_LIFETIME,
}

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('POSTGRES_DB'),
#         'USER': os.getenv('POSTGRES_USER'),
#         'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
#         'HOST': os.getenv('POSTGRES_HOST'),
#         'PORT': os.getenv('POSTGRES_PORT')
#     }
# }

###########################################################
# E-Mail Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

###########################################################

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'tr-TR'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_TZ = True

# FORMAT_MODULE_PATH = 'startup.formats'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/



STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'




# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50 MB (default is 2.5 MB)
DATA_UPLOAD_MAX_MEMORY_SIZE = 25 * 1024 * 1024  # 25 MB (default is 2.5 MB)

CORS_ORIGIN_ALLOW_ALL = True

CSRF_TRUSTED_ORIGINS = [
    "http://*",
    "https://*",
]

###########################################################
# CK-Editor-5 Settings

customColorPalette = [
        {
            'color': 'hsl(4, 90%, 58%)',
            'label': 'Red'
        },
        {
            'color': 'hsl(340, 82%, 52%)',
            'label': 'Pink'
        },
        {
            'color': 'hsl(291, 64%, 42%)',
            'label': 'Purple'
        },
        {
            'color': 'hsl(262, 52%, 47%)',
            'label': 'Deep Purple'
        },
        {
            'color': 'hsl(231, 48%, 48%)',
            'label': 'Indigo'
        },
        {
            'color': 'hsl(207, 90%, 54%)',
            'label': 'Blue'
        },
    ]

CKEDITOR_5_UPLOADS_PATH = 'ckeditor_images/'

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                    'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],
        'uploadUrl': f'{CKEDITOR_5_UPLOADS_PATH}',  # Adjust the upload path

    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
        'code','subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                    'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                    'insertTable',],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'table': {
            'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
            'tableProperties', 'tableCellProperties' ],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading' : {
            'options': [
                { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
                { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
                { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
                { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}


###########################################################
# Cross-site Scripting (XSS)

#Cross-site scripting attacks involve an attacker injecting a malicious script into your application.
#If an XSS attack is carried out, attackers may be able to steal your user's sensitive information.
#Luckily for you, you can minimize the damage of XSS attacks by adding the following lines:

# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# X_FRAME_OPTIONS = 'DENY'

############################################
# HTTS settings

# SECURE_HSTS_SECONDS = 31536000 #1 Year
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

#SECURE_HSTS_SECONDS: prevents browsers from connecting to your website with an insecure connection for the specified duration in seconds
#SECURE_HSTS_PRELOAD: the preload directive is added to the HSTS header
#SECURE_HSTS_INCLUDE_SUBDOMAINS: the includeSubDomains directive is added to the HSTS header

############################################################

# Add the following CSP settings to your settings.py file
# You can customize these settings based on your specific requirements:

# CSP_DEFAULT_SRC = ("'self'",)
# CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'", "'unsafe-eval'", "https://bursagirisimcilikzirvesi.pythonanywhere.com")
# CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", "https://fonts.googleapis.com")
# CSP_IMG_SRC = ("'self'", "data:", "https://bursagirisimcilikzirvesi.pythonanywhere.com")
# CSP_FONT_SRC = ("'self'", "https://fonts.gstatic.com")
# CSP_OBJECT_SRC = ("'none'",)
# CSP_MEDIA_SRC = ("'self'",)
# CSP_FRAME_SRC = ("'none'",)
# CSP_CONNECT_SRC = ("'self'", "https://bursagirisimcilikzirvesi.pythonanywhere.com")
# CSP_FORM_ACTION = ("'self'",)
# CSP_BASE_URI = ("'self'",)
# CSP_BLOCK_ALL_MIXED_CONTENT = True


# CSP_INCLUDE_NONCE_IN = ('script-src',)
# CSP_REPORT_URI = '/csp-report/'  # You can set a URL for CSP violation reports

# Generate a random nonce for use in 'script-src'
# CSP_NONCE = get_random_string(length=20)


############################################################
# HTTPS settings

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True  # When Deployment turn it into "True"

#SESSION_COOKIE_SECURE: ensures a secure session cookie is used
#CSRF_COOKIE_SECURE: ensures a secure CSRF cookie is used
#SECURE_SSL_REDIRECT: all non-HTTP requests are redirect to HTTPS
############################################################

# ReCaptcha Settings
#DEVELOPMENT RECAPTCHA KEYS

# RECAPTCHA_PUBLIC_KEY = '6LfdiVUpAAAAAPaBvR5hI6kCMfkx2LpyezD7gdSd'
# RECAPTCHA_PRIVATE_KEY = '6LfdiVUpAAAAAPHUGB95OFVS5WGAMGSu51sq6knA'

#PRODUCTION RECAPTCHA KEYS
# RECAPTCHA_PUBLIC_KEY = '6LdtB1ApAAAAAPOP4I8kjiyivK9NCHG8JabkX5Ww'
# RECAPTCHA_PRIVATE_KEY = '6LdtB1ApAAAAAGeD8t4E94LlhUAUmsygP5RMiGDw'

# RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')
# RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')
# RECAPTCHA_REQUIRED_SCORE = 0.5 # Eğer reCAPTCHAv3 kullanılacaksa gerekli olan alan
# SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error'] # Development ortamında Recaptcha hatası almamamak için eklendi.
######################################################