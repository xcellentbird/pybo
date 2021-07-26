from .base import *

# 보통 운영 환경을 production 환경이라고 한다.

ALLOWED_HOSTS = ['13.209.181.186']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': '.#k)nvOaa{y![#QEVSL_9go(2v_OL;N}',
        'HOST': 'ls-c7f3d71de7975f0c4b41ec2e4861bc8f96ebf85e.c3ykgqfjcvoh.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}
