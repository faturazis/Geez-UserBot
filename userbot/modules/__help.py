import logging

from userbot import BOT_USERNAME
from userbot.events import register

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.WARNING)


@register(outgoing=True, pattern=r"^\.helpme")
async def yardim(event):
    try:
        tgbotusername = BOT_USERNAME
        if tgbotusername is not None:
            results = await event.client.inline_query(tgbotusername, "@Geez-Project")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        else:
            await event.edit(
                "`Botnya tidak berfungsi! Bot Token dan Username belum di-isi/salah keless. gabisa jadinya deh.`"
            )
    except Exception:
        return await event.edit(
            "`Inline mode di bot belum aktif, aktifin dulu biar bisa cuk. (disebabkan oleh SendInlineBotResultRequest)`"
        )
