from . import reply_id as rd 

WPIC = "https://telegra.ph/file/dfd7fc05a81748a87761c.jpg"

@icss(icss_cmd(pattern="م21"))
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
@icss(
    icss_cmd(
       outgoing=True, pattern="هسمه$"
    )
)
async def kimo(tosh):
    if tosh.fwd_from:
        return
    ti = await rd(tosh)
    if WPIC:
        ics_c = f"@bot_username secret @NIIIN2 الرساله\n"
        ics_c += f"اذا تريد ترسل همسه من خلال البوت الخاص بك يجب كتابه اولا #معرف_البوت ثم #secret ثم تكتب #معرف_الي_تريد_تهمسله ثم #الرساله وستضهر ايقونه وتضغط عليها وبس 🖤✨."
        await tosh.client.send_file(tosh.chat_id, WPIC, caption=ics_c, reply_to=ti)
