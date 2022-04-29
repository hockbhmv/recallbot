import os 
import asyncio
from pyrogram import Client, idle

import logging
import logging.config
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

API_ID = os.environ.get('API_ID', '')
API_HASH = os.environ.get('API_HASH', '') 
SESSION = os.environ.get('SESSION', '')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')

bot = Client("recallbot", API_ID, API_HASH, plugins={"root": "run"}, bot_token=BOT_TOKEN)
user = Client(SESSION, API_ID, API_HASH) 

async def start():
  await user.start()
  logging.info('userbot started')
  await bot.start()
  logging.info('Bot started')
  await idle()
  await bot.stop() 
  await user.stop()
  logging.info('bot and user stopped')

loop = asyncio.get_event_loop()
loop.run_until_complete(start()) 
