import asyncio
from asyncio import wait
from telethon import events, utils

from userbot.events import register

@register(outgoing=True, pattern="^.sspam")
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        text = message.split()
        counter = int(text[1])
        spam_message = str(text[3:])
        sm = str(spam_message)
        sleep2 = int(text[2])
        await e.delete()
        for i in range(counter):
            await asyncio.wait([ 
            e.respond(sm)])
            await asyncio.sleep(sleep2)
        
