import os
from pyrogram import Client, idle

API_ID = os.environ.get('API_ID', '')
API_HASH = os.environ.get('API_HASH', '') 
SESSION = os.environ.get('SESSION', '')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')

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
