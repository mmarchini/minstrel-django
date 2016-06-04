
from minstrel.settings.base import *

DEBUG=False

ALLOWED_HOSTS = ["minstrel.me", "www.minstrel.me"]

ADMINS = [("Matheus Marchini", "matheusdot+minstrel@gmail.com")]
# MANAGERS = [("Matheus Marchini", "matheus+minstrel@gmail.com")]

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'mmarchini'
EMAIL_HOST_PASSWORD = 'ZT6qLlotaY'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
