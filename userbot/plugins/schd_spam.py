import asyncio
from asyncio import wait


from userbot.events import register

@register(outgoing=True, pattern="^.sspam")
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        text = message.split()
        counter = int(text[1])
        spam_message = str(text[2])
        sleep = int(text[3])
        for i in range(counter):
            #await asyncio.wait([ 
            e.respond(spam_message)#])
            await asyncio.sleep(0.1)
        await e.delete()
