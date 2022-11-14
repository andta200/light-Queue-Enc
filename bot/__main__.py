#    This file is part of the Compressor distribution.
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
# License can be found in
# <https://github.com/1Danish-00/CompressorQueue/blob/main/License> .


from . import *
from .devtools import *

LOGS.info("Starting...")


######## Connect ########


try:
    bot.start(bot_token=BOT_TOKEN)
except Exception as er:
    LOGS.info(er)


####### GENERAL CMDS ########


@bot.on(events.NewMessage(pattern="/start"))
async def _(e):
    await start(e)


@bot.on(events.NewMessage(pattern="/ping"))
async def _(e):
    await up(e)


@bot.on(events.NewMessage(pattern="/help"))
async def _(e):
    await help(e)


@bot.on(events.NewMessage(pattern="/link"))
async def _(e):
    await dl_link(e)


@bot.on(events.NewMessage(pattern="/restart"))
async def _(e):
    await restart(e)


@bot.on(events.NewMessage(pattern="/cancelall"))
async def _(e):
    await clean(e)


@bot.on(events.NewMessage(pattern="/showthumb"))
async def _(e):
    await getthumb(e)


@bot.on(events.NewMessage(pattern="/clear"))
async def _(e):
    await clearqueue(e)


######## Callbacks #########


@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stats(.*)")))
async def _(e):
    await stats(e)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"skip(.*)")))
async def _(e):
    await skip(e)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("ihelp")))
async def _(e):
    await ihelp(e)
    
    
@bot.on(events.callbackquery.CallbackQuery(data=re.compile("thelpbi")))
async def _(e):
    await thelpbi(e)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("thelpik")))
async def _(e):
    await thelpik(e)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("thelpuc")))
async def _(e):
    await thelpuc(e)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("thelpdo")))
async def _(e):
    await thelpdo(e)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("thelpbe")))
async def _(e):
    await thelpbe(e)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("thelpal")))
async def _(e):
    await thelpal(e)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("thelpye")))
async def _(e):
    await thelpye(e)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("thelpse")))
async def _(e):
    await thelpse(e)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("beck")))
async def _(e):
    await beck(e)


########## Direct ###########


@bot.on(events.NewMessage(pattern="/eval"))
async def _(e):
    await eval(e)


@bot.on(events.NewMessage(pattern="/bash"))
async def _(e):
    await bash(e)


@bot.on(events.NewMessage(pattern="/status"))
async def _(e):
    await status(e)


@bot.on(events.NewMessage(pattern="/get"))
async def _(e):
    await check(e)


@bot.on(events.NewMessage(pattern="/set"))
async def _(e):
    await change(e)


@bot.on(events.NewMessage(pattern="/cmds"))
async def _(e):
    await detail(e)


@bot.on(events.NewMessage(pattern="/logs"))
async def _(e):
    await getlogs(e)


########## AUTO ###########


@bot.on(events.NewMessage(incoming=True))
async def _(e):
    await thumb(e)


@bot.on(events.NewMessage(incoming=True))
async def _(e):
    await encod(e)


async def something():
    for i in itertools.count():
        try:
            if not WORKING and QUEUE:
                user = int(OWNER.split()[0])
                log = int(LOG_CHANNEL)
                e = await bot.send_message(user, "`▼ Downloading Queue Files ▼`")
                op = await bot.send_message(
                    log, "`Currently Downloading A Queued Video…`"
                )
                s = dt.now()
                try:
                    if isinstance(QUEUE[list(QUEUE.keys())[0]], str):
                        dl = await fast_download(
                            e, list(QUEUE.keys())[0], QUEUE[list(QUEUE.keys())[0]]
                        )
                    else:
                        dl, file = QUEUE[list(QUEUE.keys())[0]]
                        tt = time.time()
                        dl = "downloads/" + dl
                        with open(dl, "wb") as f:
                            ok = await download_file(
                                client=bot,
                                location=file,
                                out=f,
                                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                                    progress(
                                        d,
                                        t,
                                        e,
                                        tt,
                                        "Downloading…",
                                    )
                                ),
                            )
                except Exception as r:
                    LOGS.info(r)
                    WORKING.clear()
                    QUEUE.pop(list(QUEUE.keys())[0])
                es = dt.now()
                kk = dl.split("/")[-1]
                aa = kk.split(".")[-1]
                rr = "encode"
                bb = kk.replace(f".{aa}", ".mp4")
                out = f"{rr}/{bb}"
                thum = "thumb.jpg"
                with open("ffmpeg.txt", "r") as file:
                    ffmpeg = file.read().rstrip()
                dtime = ts(int((es - s).seconds) * 1000)
                hehe = f"{out};{dl};{list(QUEUE.keys())[0]}"
                wah = code(hehe)
                nn = await e.edit(
                    "`Encoding Files…`",
                    buttons=[
                        [Button.inline("STATS", data=f"stats{wah}")],
                        [Button.inline("CANCEL PROCESS", data=f"skip{wah}")],
                    ],
                )
                wak = await op.edit(
                    "`Currently Encoding A Queued Video…`",
                    buttons=[
                        [Button.inline("CHECK PROGRESS", data=f"stats{wah}")],
                        [Button.inline("CANCEL PROCESS", data=f"skip{wah}")],
                    ],
                )
                cmd = ffmpeg.format(dl, out)
                process = await asyncio.create_subprocess_shell(
                    cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
                )
                stdout, stderr = await process.communicate()
                er = stderr.decode()
                try:
                    if er:
                        await e.edit(str(er) + "\n\n**ERROR** Contact @danish_00")
                        QUEUE.pop(list(QUEUE.keys())[0])
                        os.remove(dl)
                        os.remove(out)
                        continue
                except BaseException:
                    pass
                ees = dt.now()
                ttt = time.time()
                await nn.delete()
                await wak.delete()
                nnn = await e.client.send_message(e.chat_id, "`▲ Uploading ▲`")
                with open(out, "rb") as f:
                    ok = await upload_file(
                        client=e.client,
                        file=f,
                        name=out,
                        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                            progress(d, t, nnn, ttt, "Uploading...")
                        ),
                    )
                fname = out.split("/")[1]
                ds = await e.client.send_file(
                    e.chat_id,
                    file=ok,
                    force_document=True,
                    caption=f"`{fname}`",
                    thumb=thum,
                )
                await nnn.delete()
                org = int(Path(dl).stat().st_size)
                com = int(Path(out).stat().st_size)
                pe = 100 - ((com / org) * 100)
                per = str(f"{pe:.2f}") + "%"
                eees = dt.now()
                x = dtime
                xx = ts(int((ees - es).seconds) * 1000)
                xxx = ts(int((eees - ees).seconds) * 1000)
                a1 = await info(dl, e)
                a2 = await info(out, e)
                dk = await ds.reply(
                    f"✅️ [Before]({a1}) • [After]({a2})\n🗜️ {hbs(com)} / {hbs(org)} • {per}\n⌛ 🔻 {x} 〽️️ {xx} 🔺 {xxx}",
                    link_preview=False,
                )
                QUEUE.pop(list(QUEUE.keys())[0])
#               await ds.forward_to(int(LOG_CHANNEL))
#               await dk.forward_to(int(LOG_CHANNEL))
                os.remove(dl)
                os.remove(out)
            else:
                await asyncio.sleep(3)
        except Exception as err:
            LOGS.info(err)


########### Start ############

LOGS.info("Bot has started.")
with bot:
    bot.loop.run_until_complete(startup())
    bot.loop.run_until_complete(something())
    bot.loop.run_forever()
