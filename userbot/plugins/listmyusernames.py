# For @UniBorg
# (c) Shrimadhav U K

from telethon import events, functions, types
from uniborg.util import admin_cmd

@borg.on(admin_cmd("listmyusernames"))
#async def handler(event):
   # if event.fwd_from:
     #   return
   # result = await borg(functions.channels.GetAdminedPublicChannelsRequest())
  #  output_str = ""
   # for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    #await event.edit(output_str)
async def mine(event):
    """ For .reserved command, get a list of your reserved usernames. """
    result = await bot(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await event.edit(output_str)
