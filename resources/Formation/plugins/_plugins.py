# Icss - UserBot
# format for plugins

import math
import os
import re
import time
import heroku3
import lottie
import requests

import spamwatch as spam_watch
from validators.url import url

from platform import python_version
from telethon import version

from userbot import *
from userbot.Config import Config
from userbot.helpers import *
from userbot.helpers import _format, _icsstools, _icssutils

# =================== Owner - Kimo ===================

USERID = bot.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
ALIVE_NAME = Config.ALIVE_NAME
AUTONAME = Config.AUTONAME
DEFAULT_BIO = Config.DEFAULT_BIO
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Icss Userbot"
BOT_USERNAME = Config.TG_BOT_USERNAME
ICSBOT = Config.TG_BOT_USERNAME
ICSB = Config.TG_BOT_USERNAME

# =================== Owner - Kimo ===================

# mention user
mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"
hmention = f"<a href = tg://user?id={USERID}>{DEFAULTUSER}</a>"

TOSHA_NAME = bot.me.first_name
TOSHA_ID = bot.me.id

# Dev tag
tosh = ( 
    "đ© đșđ¶đŒđčđȘđŹ đ±đšđœđš - đ«đŹđœđŹđłđ¶đ·đŹđč đȘ\n"
    "đčâ”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§đ»\n"
    "đâ   đ«đŹđœ đŒđșđŹđč âŹ @JAI6H àŒ\n"
    "đâ   đ«đŹđœ đ°đ« âŹ 1614314857 àŒ\n"
    "đčâ”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§đ»"
)

# Repo 
R = (
    "ââź đđđđđŸđ đđŒđđŒ - đđđđ đȘ \n"
    "đčâ”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§â”§đ»\n"
    "- đđđđđŸđ đżđđ âȘŒ [đŸđđđŸđ đđđđ](t.me/JAI6H) â©« \n"
    "- đđđđđŸđ đđđđ âȘŒ [đŸđđđŸđ đđđđ](https://github.com/JAI6H) â©«"
)
K = "https://github.com/JAI6H/ICSS-USERBOT"

# Alive Bot 
TOSH = (
       f"**ââź ŰšÙŰȘ ŰŹŰ§ÙŰ§ ÙŰčÙÙ ŰšÙŰŹŰ§Ű­ đ€â**\n"
       f"**   - Ű§Ű”ŰŻŰ§Ű± Ű§ÙŰȘÙÙŰ«ÙÙ :** `{version.__version__}\n`"
       f"**   - Ű§Ű”ŰŻŰ§Ű± ŰŹŰ§ÙŰ§ :** `{icsv}`\n"
       f"**   - Ű§ÙŰšÙŰȘ Ű§ÙÙŰłŰȘŰźŰŻÙ :** `{ICSB}`\n"
       f"**   - Ű§Ű”ŰŻŰ§Ű± Ű§ÙŰšŰ§ÙŰ«ÙÙ :** `{python_version()}\n`"
       f"**   - Ű§ÙÙŰłŰȘŰźŰŻÙ :** {mention}\n"
)

# send 
Send = "**ââź Ű§ŰłÙ Ű§ÙŰ§Ű¶Ű§ÙÙ : {}**\n**ââź Ű§ÙÙÙŰȘ Ű§ÙÙŰłŰȘŰșŰ±Ù : {}Ű«Ű§ÙÙÙ**\n**ââź ÙÙÙŰłŰȘŰźŰŻÙ :** {}"

# mybot
Mb = "**ââź Ű§ÙŰšÙŰȘ Ű§ÙÙŰłŰȘŰźŰŻÙ - {}**"

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY

thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")

PM_START = []
PMMESSAGE_CACHE = {}
PMMENU = "pmpermit_menu" not in Config.NO_LOAD

if Config.PRIVATE_GROUP_BOT_API_ID == 0:
    BOTLOG = False
    BOTLOG_CHATID = "me"
else:
    BOTLOG = True
    BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID

# Gdrive
G_DRIVE_CLIENT_ID = Config.G_DRIVE_CLIENT_ID
G_DRIVE_CLIENT_SECRET = Config.G_DRIVE_CLIENT_SECRET
G_DRIVE_DATA = Config.G_DRIVE_DATA
G_DRIVE_FOLDER_ID = Config.G_DRIVE_FOLDER_ID
TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY

# spamwatch support
if Config.SPAMWATCH_API:
    token = Config.SPAMWATCH_API
    spamwatch = spam_watch.Client(token)
else:
    spamwatch = None

ics_users = [bot.uid]
if Config.SUDO_USERS:
    for user in Config.SUDO_USERS:
        ics_users.append(user)


# ================================================

if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)


# thumb image
if Config.THUMB_IMAGE is not None:
    check = url(Config.THUMB_IMAGE)
    if check:
        try:
            with open(thumb_image_path, "wb") as f:
                f.write(requests.get(Config.THUMB_IMAGE).content)
        except Exception as e:
            LOGS.info(str(e))


def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif isinstance(dictionary[key], list):
        if value in dictionary[key]:
            return
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]


def check_data_base_heal_th():
    is_database_working = False
    output = "ÙŰ§ ŰȘÙŰŹŰŻ Ű§Ù ÙŰ§ŰčŰŻŰ© ŰšÙŰ§ÙŰ§ŰȘ"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"â {str(e)}"
        is_database_working = False
    else:
        output = "ÙŰ§ŰčŰŻÙ Ű§ÙŰšÙŰ§ÙŰ§ŰȘ ŰȘŰčÙÙ ŰšÙŰŹŰ§Ű­"
        is_database_working = True
    return is_database_working, output


async def icsa():
    _, check_sgnirts = check_data_base_heal_th()
    sudo = "Enabled" if Config.SUDO_USERS else "Disabled"
    uptime = await get_readable_time((time.time() - StartTime))
    try:
        useragent = (
            "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/80.0.3987.149 Mobile Safari/537.36"
        )
        user_id = Heroku.account().id
        headers = {
            "User-Agent": useragent,
            "Authorization": f"Bearer {Config.HEROKU_API_KEY}",
            "Accept": "application/vnd.heroku+json; version=3.account-quotas",
        }
        path = "/accounts/" + user_id + "/actions/get-quota"
        r = requests.get(heroku_api + path, headers=headers)
        result = r.json()
        quota = result["account_quota"]
        quota_used = result["quota_used"]

        # Used
        remaining_quota = quota - quota_used
        math.floor(remaining_quota / quota * 100)
        minutes_remaining = remaining_quota / 60
        hours = math.floor(minutes_remaining / 60)
        minutes = math.floor(minutes_remaining % 60)
        # Current
        App = result["apps"]
        try:
            App[0]["quota_used"]
        except IndexError:
            AppQuotaUsed = 0
        else:
            AppQuotaUsed = App[0]["quota_used"] / 60
            math.floor(App[0]["quota_used"] * 100 / quota)
        AppHours = math.floor(AppQuotaUsed / 60)
        AppMinutes = math.floor(AppQuotaUsed % 60)
        dyno = f"{AppHours}h {AppMinutes}m/{hours}h {minutes}m"
    except Exception as e:
        dyno = e
    return f"**ââź ÙŰčÙÙÙŰ§ŰȘ ŰšÙŰȘ ŰŹŰ§ÙŰ§***\
                 \n - ÙŰ§ŰčŰŻÙ Ű§ÙŰšÙŰ§ÙŰ§ŰȘ : {check_sgnirts}\
                  \n - ŰłÙŰŻÙ : {sudo}\
                  \n - ÙŰŻŰ© Ű§ÙŰȘŰŽŰșÙÙ : {uptime}\
                  \n - ÙŰŻÙ Ű§ÙŰ§ŰłŰȘŰźŰŻŰ§Ù : {dyno}\
                  "


async def make_gif(event, reply, quality=None, fps=None):
    fps = fps or 1
    quality = quality or 256
    result_p = os.path.join("temp", "animation.gif")
    animation = lottie.parsers.tgs.parse_tgs(reply)
    with open(result_p, "wb") as result:
        await _icssutils.run_sync(
            lottie.exporters.gif.export_gif, animation, result, quality, fps
        )
    return result_p
