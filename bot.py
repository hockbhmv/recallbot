import os
from pyrogram import Client, idle

API_ID = os.environ('API_ID', '')
API_HASH = os.environ('API_HASH', '') 
SESSION = os.environ('SESSION', '')
BOT_TOKEN = os.environ('BOT_TOKEN', '')

bot = Client("recallbot", API_ID, API_HASH, bot_token=BOT_TOKEN)
user = Client(SESSION, API_ID, API_HASH) 

bot.start()
print('Bot started')
user.start()
print('User started')
idle()
bot.stop()
user.stop()
print('BOTH ARE STOPPED')
