from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9_on75&ol)dcj9w(_=a_%a#5we+90b(!ac16(tfd$tivqt&#3b'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
