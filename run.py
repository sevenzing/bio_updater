import logging

from asyncio import get_event_loop, sleep

from config import CHECK_INTERVAL
from misc import client_account
from utils import is_connected
import argparse

async def internet_pooling(function, interval, **kwargs):
    max_sleep = 15 * 60
    sleep_if_no_internet = interval

    while 1:
        logging.debug(f"Run function {function.__name__}")
        if is_connected():
            sleep_if_no_internet = interval
            await function(**kwargs)
            await sleep(interval)
        else:
            logging.error(f'No internet connection. sleep for {sleep_if_no_internet} seconds')
            await sleep(min(sleep_if_no_internet, max_sleep))
            sleep_if_no_internet += interval
        

parser = argparse.ArgumentParser(description='Auto bio updater')

parser.add_argument('--mode', default='current_time', help='mode of bio updater (default: find the max)')
args = parser.parse_args()



LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -15s %(funcName) -20s: %(message)s')
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

if args.mode == 'current_time':
    function = client_account.set_time_to_bio
elif args.mode == 'time_left':
    function = client_account.set_time_left_to_bio
else:
    raise Exception('invalid mode. expected: "current_time", "time_left"')

loop = get_event_loop()

future = internet_pooling(
        function=function, 
        interval=CHECK_INTERVAL,
    )

loop.run_until_complete(future)
