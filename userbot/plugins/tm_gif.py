"""
©icss : @rruuurr
  - Tumblr Gif
  - Tumblr Gif Commends 
  - Commends of All Gif
"""

import random

from telethon import events
from .IcssGif import *

@icssbot.on(
    events.NewMessage(
       pattern=r"\.(.*)", outgoing=True
    )
)
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م20":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "**⌔∮ قائـمه اوامر المتحركات :**\n"
                "⪼ `.متحركات تمبلر`\n"
                "⪼ `.متحركات كيوت`\n"
                "⪼ `.متحركات تحشيش`\n"
                "⪼ `.متحركات جريئه`\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "**⌔∮ قائـمه اوامر المتحركات :**\n"
                "⪼ `.متحركات تمبلر`\n"
                "⪼ `.متحركات كيوت`\n"
                "⪼ `.متحركات تحشيش`\n"
                "⪼ `.متحركات جريئه`\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr) 𓆪"
            )


@icssbot.on(
    events.NewMessage(
       pattern=r"\.(.*)", outgoing=True
    )
)
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "متحركات كيوت":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "**⌔∮ قائـمه متحركات كيوت :**\n"
                "⪼ `.ك1`\n"
                "⪼ `.ك2`\n"
                "⪼ `.ك3`\n"
                "⪼ `.ك4`\n"
                "⪼ `.ك5`\n"
                "⪼ `.ك6`\n"
                "⪼ `.ك7`\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "**⌔∮ قائـمه متحركات كيوت :**\n"
                "⪼ `.ك1`\n"
                "⪼ `.ك2`\n"
                "⪼ `.ك3`\n"
                "⪼ `.ك4`\n"
                "⪼ `.ك5`\n"
                "⪼ `.ك6`\n"
                "⪼ `.ك7`\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr) 𓆪"
            )


@icssbot.on(
    events.NewMessage(
       pattern=r"\.(.*)", outgoing=True
    )
)
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "متحركات جريئه":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "**⌔∮ قائـمه متحركات جريئـه :**\n"
                "⪼ `.ج1`\n"
                "⪼ `.ج2`\n"
                "⪼ `.ج3`\n"
                "⪼ `.ج4`\n"
                "⪼ `.ج5`\n"
                "⪼ `.ج6`\n"
                "⪼ `.ج7`\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "**⌔∮ قائـمه متحركات جريئـه :**\n"
                "⪼ `.ج1`\n"
                "⪼ `.ج2`\n"
                "⪼ `.ج3`\n"
                "⪼ `.ج4`\n"
                "⪼ `.ج5`\n"
                "⪼ `.ج6`\n"
                "⪼ `.ج7`\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr) 𓆪"
            )


@icssbot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "متحركات تحشيش":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "**⌔∮ قائـمه متحركات تحشيش :**\n"
                "⪼ `.ح1`\n"
                "⪼ `.ح2`\n"
                "⪼ `.ح3`\n"
                "⪼ `.ح4`\n"
                "⪼ `.ح5`\n"
                "⪼ `.ح6`\n"
                "⪼ `.ح7`\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "**⌔∮ قائـمه متحركات تحشيش :**\n"
                "⪼ `.ح1`\n"
                "⪼ `.ح2`\n"
                "⪼ `.ح3`\n"
                "⪼ `.ح4`\n"
                "⪼ `.ح5`\n"
                "⪼ `.ح6`\n"
                "⪼ `.ح7`\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr) 𓆪"
            )


@icssbot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "متحركات تمبلر":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "⌔∮ قائـمه متحركات تمبلر :\n"
                "⪼ `.ت1`\n"
                "⪼ `.ت2`\n"
                "⪼ `.ت3`\n"
                "⪼ `.ت4`\n"
                "⪼ `.ت5`\n"
                "⪼ `.ت6`\n"
                "⪼ `.ت7`\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "⌔∮ قائـمه متحركات تمبلر :\n"
                "⪼ `.ت1`\n"
                "⪼ `.ت2`\n"
                "⪼ `.ت3`\n"
                "⪼ `.ت4`\n"
                "⪼ `.ت5`\n"
                "⪼ `.ت6`\n"
                "⪼ `.ت7`\n"
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
                "𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr) 𓆪"
            )


# ها هلو شلونك شكو ماكو شخبارك شوضعك امورك صحتك حياتك شغلاتك !


@icssbot.on(
    admin_cmd(
       outgoing=True, pattern="ت1$"
    )
)
@icssbot.on(
    sudo_cmd(
       pattern="ت1$", allow_sudo=True
    )
)
async def tmgif(kim):
    if kim.fwd_from:
        return
    kimid = await reply_id(kim)
    if tm_gif:
        kim_c = f"**{TMTE}**\n"
        kim_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        kim_c += f"**↫ المتـحركه الاولى 𓆰.**"
        await kim.client.send_file(kim.chat_id, tm_gif, caption=kim_c, reply_to=kimid)
        await kim.delete()
    else:
        await edit_or_reply(
            kim,
            f"**{TMTE}**\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
            f"**↫ المتـحركه الاولى 𓆰.**",
        )
