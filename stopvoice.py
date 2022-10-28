#!/usr/bin/python

from http import client
from telethon import TelegramClient, events
import pathlib
import os

os.chdir(pathlib.Path(__file__).parent.resolve())

api_id = os.environ['ID']
api_hash = os.environ['HASH']
username = os.environ['NAME']
client = TelegramClient(username, api_id, api_hash)

@client.on(events.NewMessage(incoming = True))
async def event_handler(event):
    whitelist = []
    if (event.chat_id > 0) and (event.chat_id not in whitelist):
        if (event.message.voice):
            await event.respond('__Пользователь ограничил функцию голосовых сообщений__')
            await client.delete_message(client.chat_id, [event.id])

#client.start(os.environ['PHONE'])
client.run_until_disconnected()