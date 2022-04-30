import os 
import json 
import logging
from config import bot, user 
from pyrogram import filters
from pyrogram.errors import InputUserDeactivated, FloodWait, UserIsBlocked, PeerIdInvalid 

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
   FRMT = "{}\n\nsucess: `{}` | `{}`\naccount deleted: `{}`\npeerid invalid: `{}`\nerror occurred: `{}`"
   try:
     group = await user.get_chat(chat_id)
     LIST = []
     total = 0
     pling = 0
     success = 0
     peerid = 0
     deleted = 0
     error = 0
     async for member in user.iter_chat_members(group.id, filter="all"):
         try:
            await msg.reply_to_message.copy(member.user.username or member.user.id) 
            success += 1
         except FloodWait as e:
            asyncio.sleep(e.x)
            await msg.reply_to_message.copy(member.user.username or member.user.id) 
            success += 1
         except InputUserDeactivated:
            deleted += 1
         except PeerIdInvalid:
            peerid += 1
         except Exception as e:
            error += 1
            print(e)
         LIST.append(f"{member.user.first_name} ({member.user.id}) [@{member.user.username}]")
         total += 1
         pling += 1
         if pling % 10 == 0:
            await edit.edit(FRMT.format("BROADCAST PROGRESSING", success, total, deleted, peerid, error))
     with open(f"{msg.from_user.id}.json", "w+") as out:
          json.dump(LIST, out) 
     await client.send_document(msg.chat.id, f"{msg.from_user.id}.json", file_name="MEMBER.json", caption="MEMBERS DETAILS")
     os.remove(f"{msg.from_user.id}.json")
     await edit.edit(FRMT.format("BROADCAST COMPLETED", success, total, deleted, peerid, error))
   except Exception as e:
     await msg.reply(e) 
