from telethon import events, Button, custom
import re, os
from userbot import bot
from . import ICSBOT

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"LEGENDX")))
async def callback_query_handler(event):
# inline by LEGENDX22 and PROBOY22 🔥
  PROBOYX = [[Button.url("REPO-LEGEND", "https://github.com/LEGENDXOP/LEGEND-BOT")]]
  PROBOYX +=[[Button.url("DEPLOY-LEGEND", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FLEGENDXOP%2Flegendpack&template=https%3A%2F%2Fgithub.com%2FLEGENDXOP%2Flegendpack")]]
  PROBOYX +=[[Button.url("TUTORIAL", "https://youtu.be/rGCSSFPsS4Q"), Button.url("STRING-SESSION", "https://repl.it/@legendx22/LEGEND-BOT#main.py")]]
  PROBOYX +=[[Button.url("API_ID & HASH", "https://t.me/usetgxbot"), Button.url("REDIS", "https://redislabs.com")]]
  PROBOYX +=[[Button.url("SUPPORT CHANNEL", "https://t.me/LEGENDBOT_OFFICIAL"), Button.url("SUPPORT GROUP", "https://t.me/LEGEND_USERBOT_SUPPORT")]]
  PROBOYX +=[[custom.Button.inline("ALIVE", data="PROBOY")]]
  await event.edit(text=f"𝙰𝙻𝙻 𝙳𝙴𝚃𝙰𝙸𝙻𝚂 𝙾𝙵 𝚁𝙴𝙿𝙾𝚂", buttons=PROBOYX)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
# inline by LEGENDX22 and PROBOY22 🔥
  LEGENDX = f"ʜᴇʟʟᴏ ᴛʜɪs ɪs  {BOT}\n\n"
  LEGENDX += "ᴀʟʟ sʏsᴛᴇᴍ ɪs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ\n\n"
  LEGENDX += f"{BOT} ᴏs : 3.0 ʟᴀsᴛᴇsᴛ\n\n"
  LEGENDX += f"ᴍʏ ᴍᴀsᴛᴇʀ @{bot.me.username} ☺️\n\n"
  LEGENDX += "ғᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ\n\n"
  LEGENDX += "ᴛᴇʟᴇᴛʜᴏɴ : 1.20 LATEST\n\n"
  LEGENDX += "ᴛʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ"
  BUTTONS = [[Button.url("𝙼𝙰𝚂𝚃𝙴𝚁", f"https://t.me/{bot.me.username}"), Button.url(f"{ICSBOT} 𝚁𝙴𝙿𝙾", "https://github.com/LEGENDXOP/LEGEND-BOT")]]
  BUTTONS += [[custom.Button.inline("𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈", data="LEGENDX")]]
  await event.edit(text=LEGENDX, buttons=BUTTONS)


@bot.on(events.NewMessage(pattern=("/repo|#repo")))
async def repo(event):
  await bot.send_message(event.chat, "ʀᴇᴘᴏ ᴏғ ʟᴇɢᴇɴᴅ-ʙᴏᴛ", buttons=[[Button.url("⚜️ ʀᴇᴘᴏ ⚜️", "https://github.com/LEGENDXOP/LEGEND-BOT")]])
