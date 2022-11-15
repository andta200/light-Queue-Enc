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
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1322549723
    LOG_CHANNEL = config("LOG_CHANNEL")
    OWNER = config("OWNER")
    FFMPEG = config(
        "FFMPEG",
#       default='ffmpeg -i "{}" -preset ultrafast -c:v libx265 -crf 27 -map 0:v -c:a aac -map 0:a -c:s copy -map 0:s? "{}"',
        default='ffmpeg -i "{}" -preset superfast -c:v libx265 -crf 28 -vf scale=640:-2 -c:a aac -vbr on -b:a 64k -threads 1 "{}"',
    )
    THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/709330fea0103f72c5d5a.jpg"
    )
    ICON = config("ICON", default="https://telegra.ph/file/251d499373a346494a26d.png")
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
