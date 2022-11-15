#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

import shutil

import psutil

from .util import get_readable_file_size
from .worker import *


async def detail(event):
    await event.reply(
        f"""
**Available Commands**
/start - __Check Bot Is Working Or Not__
/restart - __Restart Bot__
/help - __Get Detailed Help__
/get - __Get Current FFMPEG Code__
/set - __Set Current FFMPEG Code__
/cmds - __Show This List Again__
/clear - __Clear Queued Files__
/cancelall - __Clear Cached Downloads and Queued Files__
/showthumb - __Show Current Thumbnail__
/logs - __Get Bot Logs__
/status - __Get System Info__
/ping - __Check Ping__
/bash - __Run Bash Commands__
/eval - __Execute An Argument__
"""
    )


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def status(event):
    if not event.is_private:
        return
    ed = dt.now()
    currentTime = ts(int((ed - uptime).seconds) * 1000)
    total, used, free = shutil.disk_usage(".")
    total = get_readable_file_size(total)
    used = get_readable_file_size(used)
    free = get_readable_file_size(free)
    sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
    recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
    cpuUsage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    await event.reply(
        f"**Bot Uptime:** `{currentTime}`\n"
        f"**Total Disk Space:** `{total}`\n"
        f"**Used:** `{used}` "
        f"**Free:** `{free}`\n\n"
        f"**Upload:** `{sent}`\n"
        f"**Download:** `{recv}`\n\n"
        f"**CPU:** `{cpuUsage}%` "
        f"**RAM:** `{memory}%` "
        f"**DISK:** `{disk}%`"
    )


async def start(event):
    await event.reply(
        f"Hi `{event.sender.first_name}`,\n\nThis Is A Bot Which Can Encode Videos.\n\nIt's For Personal Use Only!",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.inline("YTUBE", data="thelpbi"),
                Button.inline("H264-C28", data="thelpik"),
                Button.inline("TGAUDIO", data="thelpuc"),
                Button.inline("HEVCLOGO", data="thelpdo"),           
            ],
			[
                Button.inline("HEVC720", data="thelpbe"),
                Button.inline("HEVC540", data="thelpal"),
                Button.inline("HEVC480", data="thelpye"),
                Button.inline("HEVC360", data="thelpse"),           
            ],
			[
                Button.url("SOURCE (original)", url="github.com/1Danish-00/"),
                Button.url("SOURCE (edit)", url="github.com/Col-Serra/light-Queue-Enc"),
            ],
            [Button.url("CHANNEL️", url="t.me/tgyararlibotlar")],
        ],
    )


async def help(event):
    await event.reply(
        "**SET EXAMPLE:**\n`/set ffmpeg -i '''{}''' -preset superfast -c:v libx265 -crf 28 -c:a aac -vbr on -b:a 64k -s 640x360 -threads 1 '''{}'''`\n\n🖍 ️`-c:v libx264 -pix_fmt yuv420p`\n\n🖍 ️`-vf scale=640:-2`\n\n🖍 ️`-vf '''drawtext=fontfile=font.ttf:fontsize=30:fontcolor=white:bordercolor=black@0.50:x=w/2-tw/2:y=10:box=1:boxcolor=black@0.5:boxborderw=6:text=Konuşanlar TV'''`"
    )


async def ihelp(event):
    await event.edit(
        "**SET EXAMPLE:**\n`/set ffmpeg -i '''{}''' -preset superfast -c:v libx265 -crf 28 -c:a aac -vbr on -b:a 64k -s 640x360 -threads 1 '''{}'''`\n\n🖍 ️`-c:v libx264 -pix_fmt yuv420p`\n\n🖍 ️`-vf scale=640:-2`\n\n🖍 ️`-vf '''drawtext=fontfile=font.ttf:fontsize=30:fontcolor=white:bordercolor=black@0.50:x=w/2-tw/2:y=10:box=1:boxcolor=black@0.5:boxborderw=6:text=Konuşanlar TV'''`",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def thelpbi(event):
    await event.edit(
        "`/set ffmpeg -i '''{}''' -preset superfast -c:v libx264 -pix_fmt yuv420p -crf 20 -c:a aac -vbr on -b:a 128k -vf scale=1280:-2 -threads 1 '''{}'''`",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def thelpik(event):
    await event.edit(
         "`/set ffmpeg -i '''{}''' -preset superfast -c:v libx264 -pix_fmt yuv420p -crf 28 -c:a aac -vbr on -b:a 128k -vf scale=1280:-2 -threads 1 '''{}'''`",
        buttons=[Button.inline("BACK", data="beck")],
    )

async def thelpuc(event):
    await event.edit(
        "`/set ffmpeg -i '''{}''' -c:a aac -vbr on b:a 128k -threads 1 '''{}'''`",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def thelpdo(event):
    await event.edit(
        "`/set ffmpeg -i '''{}''' -preset superfast -c:v libx265 -crf 28 -c:a aac -vbr on -b:a 64k -s 1280x720 -vf '''drawtext=fontfile=font.ttf:fontsize=30:fontcolor=white:bordercolor=black@0.50:x=w/2-tw/2:y=10:box=1:boxcolor=black@0.5:boxborderw=6:text=Konuşanlar TV''' -threads 1 '''{}'''`",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def thelpbe(event):
    await event.edit(
        "`/set ffmpeg -i '''{}''' -preset superfast -c:v libx265 -crf 28 -c:a aac -vbr on -b:a 64k -vf scale=1280:-2 -threads 1 '''{}'''`",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def thelpal(event):
    await event.edit(
        "`/set ffmpeg -i '''{}''' -preset superfast -c:v libx265 -crf 28 -c:a aac -vbr on -b:a 64k -vf scale=960:-2 -threads 1 '''{}'''`",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def thelpye(event):
    await event.edit(
        "`/set ffmpeg -i '''{}''' -preset superfast -c:v libx265 -crf 28 -c:a aac -vbr on -b:a 64k -vf scale=854:-2 -threads 1 '''{}'''`",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def thelpse(event):
    await event.edit(
        "`/set ffmpeg -i '''{}''' -preset superfast -c:v libx265 -crf 28 -c:a aac -vbr on -b:a 64k -vf scale=640:-2 -threads 1 '''{}'''`",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def beck(event):
    await event.edit(
        f"Hi `{event.sender.first_name}`,\n\nThis Is A Bot Which Can Encode Videos.\n\nIt's For Personal Use Only!",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.inline("YTUBE", data="thelpbi"),
                Button.inline("H264-C28", data="thelpik"),
                Button.inline("TGAUDIO", data="thelpuc"),
                Button.inline("HEVCLOGO", data="thelpdo"),           
            ],
			[
                Button.inline("HEVC720", data="thelpbe"),
                Button.inline("HEVC540", data="thelpal"),
                Button.inline("HEVC480", data="thelpye"),
                Button.inline("HEVC360", data="thelpse"),           
            ],
			[
                Button.url("SOURCE (original)", url="github.com/1Danish-00/"),
                Button.url("SOURCE (edit)", url="github.com/Col-Serra/light-Queue-Enc"),
            ],
            [Button.url("CHANNEL️", url="t.me/tgyararlibotlar")],
        ],
    )
