# Hi


DEFULTUSER = ALIVE_NAME or "ICSS"
TG_BOT = Config.TG_BOT_USERNAME

Hi = (
    "⌔∮ 𝑰𝑪𝑺𝑺 𝑯𝑨𝑺 𝑫𝑬𝑷𝑳𝑶𝒀𝑬𝑫",
    "➖➖➖➖➖➖➖➖➖\n",
    "- 𝑼𝒔𝒆𝒓𝑵𝒂𝒎𝒆 : {mention}",
    "- 𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕 : {TG_BOT}",
    "➖➖➖➖➖➖➖➖➖",
    "- 𝑺𝒖𝒑𝒑𝒐𝒓𝒕: @rruuurr",
    "➖➖➖➖➖➖➖➖➖",
)


@icssbot.on(admin_cmd(pattern="هها"))
async def icss(dev):
    await div.edit(Hi)
