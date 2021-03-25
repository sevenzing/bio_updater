from config import credentials, CHECK_INTERVAL
from utils import is_connected
from client import Client
from asyncio import run_coroutine_threadsafe, get_event_loop, sleep
import logging


async def internet_pooling(function, interval, kwargs):
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


client = Client(**credentials, try_logging_in=True)
print(client)

loop = get_event_loop()

future = internet_pooling(
        function=Client.set_time_to_bio, 
        interval=CHECK_INTERVAL,
        kwargs={
            'self': client,
            })

loop.run_until_complete(future)
