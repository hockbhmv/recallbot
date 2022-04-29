import os 
from pyrogram import Client 

API_ID = os.environ.get('API_ID', '')
API_HASH = os.environ.get('API_HASH', '') 
SESSION = os.environ.get('SESSION', '')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')

bot = Client("recallbot", API_ID, API_HASH, plugins={"root": "run"}, bot_token=BOT_TOKEN)
user = Client(SESSION, API_ID, API_HASH) 
