import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from pyrogram import Client, filters

from config import HNDLR, SUDO_USERS



# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["jkwkskjsjwnnjajajjwnwjajns"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("⚡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>Tôi đang trực tuyến🍀</b> `{delta_ping * 100:.3f} ms` \n<b>⏳Thời Gian Hoạt Động </b> - `{uptime}`"
    )


@Client.on_message(filters.command(["hotro"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
**🤓Xin Chào {m.from_user.mention}!

🛠 HỖ TRỢ MENU
⚡ LỆNH CƠ BẢN
❍ {HNDLR}hotro - để xem danh sách các lệnh
❍ {HNDLR}play [tên bài hát | liên kết youtube | trả lời tệp âm thanh] - để phát một bài hát
❍ {HNDLR}vplay [tiêu đề video | liên kết youtube | trả lời tệp video] - để phát video
❍ {HNDLR}danhs để xem danh sách phát
❍ {HNDLR}ping - để kiểm tra trạng thái
❍ {HNDLR}tieptuc - để tiếp tục phát một bài hát hoặc video
❍ {HNDLR}dunglai - để tạm dừng phát lại một bài hát hoặc video
❍ {HNDLR}boqua - để bỏ qua các bài hát hoặc video
❍ {HNDLR}tat - để kết thúc phát lại**
"""
    await m.reply(HELP)






@Client.on_message(filters.command(["", "", "", "", ""], prefixes=f"{HNDLR}"))
async def goodnight(client, m: Message):
    
    GN = f"""
<i>Nếu Như Mày Có Ý Định Chê Bot Thì Nín Tao Bắt Quả Tang Mày Rồi  </i>
"""
    await m.reply(GN)
