## Icss - Userbot

هذه هي اضافات اكسس بوت ماخوذه من عدة سورسرات وقمت بتعديلها وعربتها لكي يصبح ﭑڪثر جماليه وقمت باضافات جميله مثل الاسماء الجاهزه والمتحركات وغيرها 

## Formation

الآن سأظهر نص قصير لإظهار تكوين البرنامج النصي المطلوب.
```python3
@icssbot.on(icss_cmd(pattern="اكسس", outgoing=True))
@icssbot.on(sudo_cmd(pattern="اكسس", outgoing=True))
async def icsbot(kim):
    if kim.fwd_from:
        return
    await eor(kim , "**- اهلا بك في بوت اكسس**\n- هذا بوت معرب من اجلك استمتع" + Config.SUDO_USERS)
```

- استمتعو به 💕
- ANL0KE ( [DEV-SOURCE](https://t.me/rruuurr) )
