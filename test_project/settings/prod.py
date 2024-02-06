from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

HOST_NAME = os.getenv("HOST_NAME")

ALLOWED_HOSTS = [HOST_NAME]
