from . import reply_id as rd
from userbot.kimo import *


WPIC = "https://telegra.ph/file/dfd7fc05a81748a87761c.jpg"


@icssbot.on(icss_cmd(pattern="م21"))
async def wspr(kimo):
    await kimo.edit(
        "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑺𝑬𝑪𝑹𝑬𝑻 𝑴𝑺𝑮 𓆪\n"
        "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        "**⌔∮ قائـمه اوامر الهمسه :** \n"
        "⪼ `.همسه` لعرض كيفيه ارسال همسه \n"
        "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        "𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr) 𓆪"
    )


# Wespr - همسه
@icssbot.on(icss_cmd(outgoing=True, pattern="همسه$"))
async def kimo(lon):
    if lon.fwd_from:
        return
    ld = await rd(lon)
    if WPIC:
        ics_c = f"اذا تريد ترسل همسه من خلال البوت الخاص بك يجب كتابه اولا #معرف_البوت ثم #secret ثم تكتب #معرف_الي_تريد_تهمسله ثم #الرساله وستضهر ايقونه وتضغط عليها وبس 🖤✨.\n"
        ics_c += f"**- قم بنسخ :**\n `{ICSB} secret @NIIIN2 الرساله`"
        await lon.client.send_file(lon.chat_id, WPIC, caption=ics_c, reply_to=ld)
