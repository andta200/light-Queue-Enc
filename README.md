# Queue Encoder Bot (For Single Users) 
*doesn't work in groups yet pull requests to change that are welcomed*

## Variables
`APP_ID` `API_HASH` `BOT_TOKEN`

`OWNER` : Enter The Id Of Auth Users with a spaces between it

`LOG_CHANNEL` : The Id Of your Log Channel Or Group Goes Here

`THUMBNAIL` : Enter telegraph link of a picture for use as Thumbnail.

`ICON` : Enter The Telegraph link of a picture (png) for use as watermaking image.

`FFMPEG` : Put Your FFMPEG Code with """{}""" as input and output *(Remember to excape the special characters in the case of local deployment to avoid errors)* . (Eg. `ffmpeg -i """{}""" -preset veryfast -vcodec libx265 -crf 27 """{}"""`) *(Also Use this Format When changing code via /set command)*

- [Main Source](https://github.com/1Danish-00/CompressorBot)

### Commands:
```
start - Check Bot Is Working Or Not
restart - Restart Bot
help - Get Detailed Help
get - Get Current FFmpeg Code
set - Set Custom FFmpeg Code
cmds - List Available Commands
clear - Clear Queued Files
cancelall - Clear Cached Downloads & Queued Files
showthumb - Show Current Thumbnail
logs - Get Bot Logs
status - Bot Status
ping - Check Ping
bash - Run Bash Commands
eval - Execute An Argument

```
### Default Audio Language:
- 1. Language:
```

/set ffmpeg -i '''{}''' -preset superfast -c:v libx265 -crf 28 -c:a aac -vbr on -b:a 64k -vf scale=640:-2 -map 0:v:1 -map 0:a:0 -threads 1 '''{}'''

```

- 2. Language: 🆗🇹🇷
```

/set ffmpeg -i '''{}''' -preset superfast -c:v libx265 -crf 28 -c:a aac -vbr on -b:a 64k -vf scale=640:-2 -map 0:v:1 -map 0:a:1 -threads 1 '''{}'''

```
