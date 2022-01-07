import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/ed27010abc3804bebbddd.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Xin Chào [{event.sender.first_name}](tg://user?id={event.sender.id}), Tôi Là OGGY VXer2 BOT.** \n\n"
  TEXT += "💠 **Tôi đang hoạt động ** \n\n"
  TEXT += f"💠 **Chủ Nhân Của Tôi : [OGGY VN](https://t.me/oggyvn)** \n\n"
  TEXT += f"💠 **Phiên bản Thư viện :** `{telever}` \n\n"
  TEXT += f"💠 **Phiên bản Telethon :** `{tlhver}` \n\n"
  TEXT += f"💠 **Phiên bản Pyrogram :** `{pyrover}` \n\n"
  TEXT += "**Cảm ơn vì đã sử dụng BOT OGGY VXer2 ❤️**"
  BUTTON = [[Button.url("Lệnh BOT", "https://t.me/oggyvietnam_bot?start=help"), Button.url("OGGY VN", "https://t.me/OGGYVN")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
