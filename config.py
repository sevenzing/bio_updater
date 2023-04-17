import datetime
import pytz

from credentials import credentials


CHECK_INTERVAL = 3

TIME_ZONE = 'Etc/GMT-3'

INTERNET_CHECK_URL = '1.1.1.1'

BIO_MESSAGES = [
    'Сейчас %s',
    'Уже %s',
    '%s',
]

DATE_FROM = datetime.datetime(2022, 2, 24, 3, 0, 0, tzinfo=pytz.UTC) 

TIME_LEFT_MESSAGE = 'Прошло уже %s'