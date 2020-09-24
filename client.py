from telethon import TelegramClient, events, sync
from telethon.tl.types import Dialog
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.account import UpdateProfileRequest
from typing import List, Dict
import re
import logging

from config import BIO_MESSAGE
from time_tools import get_current_time_in_words, get_now
from asyncio import sleep
from datetime import timedelta

class Client:
    def __init__(self, session, api_id, api_hash, try_logging_in=False):
        self.session = session
        self.api_id = api_id
        self.api_hash =  api_hash 
        self.account = TelegramClient(session, api_id, api_hash)
        self.account.connect()
        self.lastupdate = get_now() - timedelta(minutes=1)
        if try_logging_in:
            self.account.start()

    async def edit_bio(self, new_bio):
        logging.debug('check for changing bio')
        # 1 minute
        try:
            if get_now().minute != self.lastupdate.minute:
                logging.info(f"Change bio to {new_bio}")
                await self.account(UpdateProfileRequest(
                    about=new_bio,
                ))
                self.lastupdate = get_now()
        except FloodWaitError as e:
            logging.warning(f"Got flood message: {e}. sleep for {e.seconds}")
            await sleep(e.seconds)

    async def set_time_to_bio(self):
        await self.edit_bio(BIO_MESSAGE % get_current_time_in_words())

    def __str__(self):
        me = self.account.get_me()
        return f"TelegramClient({me.first_name} {me.last_name}, @{me.username})"
