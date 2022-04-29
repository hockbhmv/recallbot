import os 
import json 
import logging
from config import bot, user 
from pyrogram import filters

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR) 

@bot.on_message(filters.command('start') & filters.private)
async def start(bot, msg):
   await msg.reply('Bot working successfully')
  
@bot.on_message(filters.command('request') & filters.private)
async def request(client, msg):
   if len(msg.command) < 2:
      return await msg.reply_text('provide chat id or username')
   chat_id = msg.command[1]
   edit = await msg.reply('.......')
   try:
     group = await user.get_chat(chat_id)
   except Exception as e:
     await msg.reply(e)
   async for member in user.iter_chat_members(chat.id, filter="all"):
      LIST = []
      total = 0
      pling = 0
      LIST.append(f"{member.first_name} ({member.id}) [@{member.username}]")
      total += 1
      pling += 1
      if pling % 10 == 0:
          await edit.edit(f"completed: {total}")
   with open(f"{msg.from_user.id}.json", "w+") as out:
        json.dump(LIST, out) 
   await client.send_document(msg.chat.id, f"{msg.from_user.id}.json", file_name="MEMBER.json", caption="MEMBERS DETAILS")
   os.remove(f"{msg.from_user.id}.json")
   await edit.edit(f"completed: {total}")
