import asyncio
from asyncio import wait


from userbot.events import register

@register(outgoing=True, pattern="^.spam")
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(text[1])
        spam_message = str(text[2])
        sleep = int(text[3])
        await asyncio.wait([ 
        for i in range(counter):
            e.respond(spam_message)
            await asyncio.sleep(0.1)])
        await e.delete()
