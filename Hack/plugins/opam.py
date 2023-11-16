import env
from Hack import bot
from Hack.helpers import MENU1, KEYBOARD1
from Hack.database import DB
from telethon import events
from telethon.tl.custom.button import Button
from telethon import TelegramClient, events
OWNER_ID = 6204761408  
@bot.on(events.NewMessage)
async def on_pm_s(event):
    if not event.is_private:
        return
    if not event.sender_id == OWNER_ID:
        fwded_mesg = await event.forward_to(OWNER_ID, silent=True)
