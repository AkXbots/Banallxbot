# Powered by @Darkranger00 | TELE:- @aadillllll
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by Aadil Shiekh
import logging
import re
import os
import sys, platform
# import functie as S
from asyncio import sleep
from os import getenv
from dotenv import load_dotenv
from telethon import TelegramClient, events, Button
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon import __version__ as tel
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from str import dad as gg, dady as g, startxt2, startxt, hlptxt
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime

#Logging...
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
API_ID = 28199914
API_HASH = "0a6ed84fc63109ce1c8fbfa61ab2ea7b"
BOT_TOKEN = "6058362069:AAFZD8Fwsqgz0iKudikq-vDllNsedQci8Fg"
OWNER_ID = "6221752209"
SUDO_ID = "6278515974"
LUCIFER = "6515946748"
COWNER_ID = "6156148673"
OP  = [ int(OWNER_ID), int(SUDO_ID), int(COWNER_ID), int(LUCIFER)]
#TelegramClient..
sree = TelegramClient(
    "BanAll",
    api_id=API_ID,
    api_hash=API_HASH
).start(bot_token=BOT_TOKEN)

Owner = "DeityRuler"
repo = "https://t.me/Bonten_destroyers"
@sree.on(events.NewMessage(pattern="^/start"))
async def start(event):
    buttns = [Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/bonten_mainchats"), Button.url(" • ᴄʜᴀɴɴᴇʟ •", "https://t.me/Bonten_Destroyers")]
    py = platform.python_version()
    if event.sender.id in OP:
        await sree.send_file(
            event.chat.id,
            file="https://telegra.ph/file/7efb1c4feb25433d5d86e.jpg",
            caption=startxt.format(
                event.sender.first_name,
                event.sender.id,
                py,
                tel,
                Owner,
            ),
            link_preview=False,
            buttons=buttns
        )
    if event.sender.id not in OP:
        await sree.send_file(
            event.chat.id,
            file="https://telegra.ph/file/106fa1aca8074465452d2.jpg",
            caption=startxt2.format(
                event.sender.first_name,
                event.sender.id,
                py,
                tel,
                Owner,
            ),
            link_preview=False,
            buttons=buttns
        )


@sree.on(events.NewMessage(pattern="^/help"))
async def start(event):
    buttns = [Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/bonten_mainchats"), Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/Bonten_Destroyers")]   
    py = platform.python_version()  
    if event.sender.id in OP:
        await sree.send_file(
            event.chat.id,
            file="https://telegra.ph/file/534103edc6bca310d19ea.jpg",
            caption=hlptxt.format(event.sender.first_name, event.sender.id),
            link_preview=False,
            buttons=buttns
        )
    if event.sender.id not in OP:
        await event.reply(
            "Huh Nigga!\nᴛʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ.)",
            link_preview=False,
        )       

@sree.on(events.NewMessage(pattern="^/ping"))
async def ping(event):
    if event.sender.id in OP:
        start = datetime.now()
        t = "Pinging..."
        txxt = await event.reply(t)
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await txxt.edit(f"ɪ'ᴍ ᴀʟɪᴠᴇ.... !!\n\nᴘɪɴɢ ᴘᴏɴɢ...\n   ➥ `{ms} ms`")


@sree.on(events.NewMessage(pattern="^/banall"))
async def bun(event):
  if event.sender.id in OP:
   if not event.is_group:
        Rep = f"__ᴡᴛғ ʙʀᴏ 🙄.\nUse ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪɴ ᴀɴʏ ɢʀᴏᴜᴘ!! __"
        await event.reply(Rep) 
   else:
       await event.delete()
       cht = await event.get_chat()
       boss = await event.client.get_me()
       admin = cht.admin_rights
       creator = cht.creator
       if not admin and not creator:
           await event.reply("__ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ sᴜғғɪᴄɪᴇɴᴛ ʀɪɢʜᴛs ᴛᴏ ᴅᴏ ᴛʜɪs.__")
           return
       hmm =  await event.reply("ɪ'ᴍ ғᴜᴄᴋɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘ!! :- @Bonten_Destroyers")
       await sleep(18)
       await hmm.delete()
       everyone = await event.client.get_participants(event.chat_id)
       for user in everyone:
           if user.id == boss.id:
               pass
           try:
               await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
           except Exception as e:
               await event.edit(str(e))
           await sleep(0.3)


@sree.on(events.NewMessage(pattern="^/restart"))
async def restart(jnl):
    if jnl.sender.id in OP:
        tct = "__ᴡᴀɪᴛ ʟᴇᴀᴠɪɴɢ...__"
        await jnl.reply(tct)
        try:
            await sree.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


@sree.on(events.NewMessage(pattern="^/leave"))
async def leave(z):
    if z.sender.id in OP:
        mkc = ("".join(z.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(z.text) > 7:
            mkb = int(mkc[0])
            tet = "__ᴡᴀɪᴛ ʟᴇᴀᴠɪɴɢ...__"
            hm = await z.reply(tet)
            try:
                await z.client(LeaveChannelRequest(mkb))
                await hm.edit("**₴Ʉ₵₵Ɇ₴₴₣ɄⱠⱠɎ ⱠɆ₣₮ɆĐ!!**")
            except Exception as e:
                await hm.edit(str(e))
        else:
            mkb = z.chat_id
            txt = "__ᴡᴀɪᴛ ʟᴇᴀᴠɪɴɢ...__"
            ok = await z.reply(txt)
            try:
                await z.client(LeaveChannelRequest(mkb))
                await ok.edit("**₴Ʉ₵₵Ɇ₴₴₣ɄⱠⱠɎ ⱠɆ₣₮ɆĐ!!**")
            except Exception as e:
                await z.edit(str(e))

@sree.on(events.NewMessage)
async def ver(events):
    events = S
    await events.main(str(e))


print("Your Bot  Deployed Successfully ✅")
print("Join @crushbot_support if you facing any kind of issue!!")



sree.run_until_disconnected()
