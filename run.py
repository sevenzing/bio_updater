from config import credentials, CHECK_INTERVAL
from client import Client
from asyncio import run_coroutine_threadsafe, get_event_loop, sleep
import logging

async def forever(function, interval, args):
    while 1:
        logging.debug(f"Run function {function.__name__}")
        await function(**args)
        await sleep(interval)


LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -15s %(funcName) -20s: %(message)s')
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

account_cridentials = credentials['lev']

client = Client(**account_cridentials, try_logging_in=True)
print(client)

loop = get_event_loop()

loop.create_task(forever(
        function=Client.set_time_to_bio, 
        interval=CHECK_INTERVAL,
        args={
            'self': client,
            }))


loop.run_forever()