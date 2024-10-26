from pyrogram import Client, idle
#'‹ ٰ💸 ⇣ حمودي سورس ⇣ 💸 › .'#
from pyromod import listen



bot = Client(
    "mo",
    api_id=24944052,
    api_hash="a5629d152074e82aa8795953a7f665a7",
    bot_token="8058386608:AAH0l7VGtQi-zUYC6LREMFH48GqWdPyPBkA",#توكن المصنع
    plugins=dict(root="MHelal")
    )

async def start_helalbot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    hh = "@nn66O"#يوزر المطور المصنع
    try:
        await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
    except:
        pass
    await idle()
