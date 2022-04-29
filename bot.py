import os 
import asyncio 
from congfig import bot, user
from pyrogram import Client, idle

import logging
import logging.config
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

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
