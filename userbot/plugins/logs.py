##########################

# Made By Unknown Person######

##########################

# Fixed by @TechnoAyanOfficial  ##

##########################

# © TechnoAyanBot 2020 #######

##########################

from userbot.events import register

import heroku3

import aiohttp

import math

import asyncio

import os

from userbot import (

    CMD_HELP,

    BOTLOG,

    BOTLOG_CHATID

)

HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)

HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

@register(outgoing=True, pattern=r"^\.logs")

async def _(dyno):

        try:

             Heroku = heroku3.from_key(HEROKU_API_KEY)

             app = Heroku.app(HEROKU_APP_NAME)

        except:

  	       return await dyno.reply("`Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var.`")        await dyno.edit("`Getting Logs....`")

        with open('logs.txt', 'w') as log:

            log.write(app.get_log())

        await dyno.client.send_file(

            dyno.chat_id,

            "logs.txt",

            reply_to=dyno.id,

            caption="Here's your heroku dyno logs"

        )

        await asyncio.sleep(5)

        await dyno.delete()

        return os.remove('logs.txt')
