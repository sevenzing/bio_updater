import os


credentials = {
    'lev':{
        'api_id': 1,
        'api_hash': '1',
        'session': 'account0.session'
    }
}

CHECK_INTERVAL = int(os.environ.get('CHECK_INTERVAL', ''))

TIME_ZONE = os.getenv('TIME_ZONE', '')

BIO_MESSAGE = 'Сейчас %s.'