import logging

from asyncio import get_event_loop, sleep

from config import CHECK_INTERVAL
from misc import client_account
from utils import is_connected


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
        


LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -15s %(funcName) -20s: %(message)s')
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

print(client_account)

loop = get_event_loop()

future = internet_pooling(
        function=client_account.set_time_left_to_bio, 
        interval=CHECK_INTERVAL,
    )

loop.run_until_complete(future)
