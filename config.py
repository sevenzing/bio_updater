import os
from credentials import credentials

CHECK_INTERVAL = int(os.environ.get('CHECK_INTERVAL', ''))

TIME_ZONE = os.getenv('TIME_ZONE', '')

BIO_MESSAGE = 'Сейчас %s.'