
""" stats plugin """

from datetime import datetime

from pyrogram.types import Message
from pyrogram.enums import ChatType

from deadly import app, gen




app.CMD_HELP.update(
    {"stats": (
        "stats",
        {
        "stats" : "Get information about how many groups/channels/users you have in your dialogs."
        }
        )
    }
)



@app.on_message(gen("stats"))
async def stats(client, message):
    """ dialogstats handler for stats plugin """
    try:
        start = datetime.now()
        await app.send_edit("Getting stats . . .", text_type=["mono"])

        bot = 0
        user = 0
        group = 0
        channel = 0        
        supergroup = 0
        stats_format = """
• **𝗦𝗧𝗔𝗧𝗦 𝗙𝗢𝗥:** {}\n\n
𝗬𝗼𝘂𝗿 𝗦𝘁𝗮𝘁𝘀 𝗢𝗯𝘁𝗮𝗶𝗻𝗲𝗱 𝗶𝗻 {} 𝘀𝗲𝗰𝗼𝗻𝗱𝘀\n\n
𝗬𝗼𝘂  𝗵𝗮𝘃𝗲 {} 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗠𝗲𝘀𝘀𝗮𝗴𝗲𝘀.\n
𝗬𝗼𝘂 𝗮𝗿𝗲 𝗶𝗻 {} 𝗚𝗿𝗼𝘂𝗽𝘀.\n
𝗬𝗼𝘂 𝗮𝗿𝗲 𝗶𝗻 {} 𝗦𝘂𝗽𝗲𝗿 𝗚𝗿𝗼𝘂𝗽𝘀.\n
𝗬𝗼𝘂 𝗔𝗿𝗲 𝗶𝗻 {} 𝗖𝗵𝗮𝗻𝗻𝗲𝗹𝘀.\n
𝗕𝗼𝘁𝘀 = {}\n\n
𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗯𝘆: @DeadlyUserbot
"""

        async for dialog in client.get_dialogs():
            if dialog.chat.type == ChatType.CHANNEL:
                channel += 1
            if dialog.chat.type == ChatType.BOT:
                bot += 1
            if dialog.chat.type == ChatType.GROUP:
                group += 1
            if dialog.chat.type  == ChatType.SUPERGROUP:
                supergroup += 1                
            if dialog.chat.type == ChatType.PRIVATE:
                user += 1
        end = datetime.now()
        ms = (end - start).seconds     
        await app.send_edit(stats_format.format(app.UserMention(), ms, user, group, supergroup, channel, bot))
    except Exception as e:
        await app.error(e)
