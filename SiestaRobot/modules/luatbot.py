import asyncio
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, version
from SiestaRobot.events import register
from SiestaRobot import telethn as aasf
from SiestaRobot import StartTime, dispatcher

edit_time = 5
""" =======================2022====================== """
luatbot1 = "https://telegra.ph/file/ee0fa410c0414a650f673.jpg"
luatbot2 = "https://telegra.ph/file/ee0fa410c0414a650f673.jpg"
luatbot3 = "https://telegra.ph/file/ee0fa410c0414a650f673.jpg"
luatbot4 = "https://telegra.ph/file/789d31689646320c217c3.jpg"
luatbot5 = "https://telegra.ph/file/b8e2f6eff4ddd608561d8.jpg"
""" =======================2022====================== """

@register(pattern=("/luatbot"))
async def hmm(event):
    chat = await event.get_chat()
    await event.delete()
    pm_caption = f"**Luật BOT OGGY VN **\n\n"
    pm_caption += "**1.Không Lạm quyền bot,không ban hoặc mute cá nhân nào khi không có lí do\n2.Sử dụng bot văn minh không spam tin nhắn bot không cố tình phá hoại bot tập thể\n3.Hãy là người có ý thức bảo vệ văn hoá tránh những logic sai suy nghĩ của người khác\n Cảm Ơn Bởi OGVN Team**\n\n"
    on = await aasf.send_file(event.chat_id, file=luatbot1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await aasf.edit_message(event.chat_id, on, file=luatbot2) 

    await asyncio.sleep(edit_time)
    ok2 = await aasf.edit_message(event.chat_id, ok, file=luatbot3)

    await asyncio.sleep(edit_time)
    ok3 = await aasf.edit_message(event.chat_id, ok2, file=luatbot4)
    
    await asyncio.sleep(edit_time)
    ok4 = await aasf.edit_message(event.chat_id, ok3, file=luatbot1)
    
    await asyncio.sleep(edit_time)
    ok5 = await aasf.edit_message(event.chat_id, ok4, file=luatbot2)
    
    await asyncio.sleep(edit_time)
    ok6 = await aasf.edit_message(event.chat_id, ok5, file=luatbot3)
    
    await asyncio.sleep(edit_time)
    ok7 = await aasf.edit_message(event.chat_id, ok6, file=luatbot4)
    
    await asyncio.sleep(edit_time)
    ok8 = await aasf.edit_message(event.chat_id, ok7, file=luatbot5)
