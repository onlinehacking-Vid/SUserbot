# all import loads here and plugins 

import sys
import asyncio
import warnings
from pyrogram import idle
from pyrogram.types import (
    BotCommand,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from pyrogram.errors import (
    PeerIdInvalid,
    ChannelInvalid
)
from deadly.client import app




async def start_assistant():
    """ this function starts the pyrogram bot client. """
    if app and app.bot:
        print("Activating assistant client...\n")
        response = await app.bot.start()
        if response:
            print("Assistant activated Successfully...\n")
            botcmd = [
                ["start", "check whether bot is on or not."],
                ["help", "Get your help menu of bot."],
                ["ping", "Get server response speed & uptime."],
                ["id", "Get ids of users / groups."],
                ["quote", "get inline anime quotes."],
                ["broadcast", "send messages to users who have started your bot."],
                ["eval", "evaluate python codes."]
            ]
            cmds = [x.command for x in await app.bot.get_bot_commands()]
            botcmdkeys = [y[0] for y in botcmd]

            if cmds != botcmdkeys:
                print("Setting bot commands.\n")
                await app.bot.set_bot_commands([BotCommand(y[0], y[1]) for y in botcmd])
                print("Added bot commands.\n")
        else:
            print("Assistant is not activated..\n")
    else:
        print("Assistant start unsuccessful, please check that you have given the correct bot token.\n")
        print("skipping assistant start !")



async def start_userbot():
    """ this function starts the pyrogram userbot client. """
    if app:
        print("Activating userbot Client..\n")
        response = await app.start()
        if response:
            print("Userbot activated Successfully.\n")
        else:
            print("Userbot is not activated.\n")
    else:
        print("Userbot startup unsuccessful, please check everything again ...")
        print("Quiting ...")
        sys.exit()




async def send_logmessage():
    await app.bot.send_message(
        app.LOG_CHAT,
        "The DeadlyUserbot is online now.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Support Group",
                        url="t.me/TheDeadlyBots"
                    )
                ]
            ]
        )
    )




async def start_bot():
    """ This is the main startup function to start both clients i.e assistant & userbot.
    It also imports modules & plugins for assistant bot & userbot. """

    print(20*"_" + ". Welcome to Deadly Network." + "_"*20 + "\n\n\n")
    print("PLUGINS: Installing..\n\n")
    botplugins = app.import_module("deadly/modules/assistant/plugins/", exclude=app.NoLoad())
    app.import_module("deadly/modules/assistant/callbacks/", display_module=False)
    app.import_module("deadly/modules/assistant/Inlinequeries/", display_module=False)
    print(f"\n\n{botplugins} plugins Loaded Successfully\n\n")
    print("MODULES: Installing..\n\n")
    plugins = app.import_module("deadly/modules/userbot/", exclude=app.NoLoad())
    print(f"\n\n{plugins} modules Loaded Successfully\n\n")
    await start_assistant()
    await start_userbot()
    print("Your DeadlyUserbot Started Successfully, try .ping or .alive commands to test it.")

    try:
        await send_logmessage()
    except (ChannelInvalid, PeerIdInvalid):
        try:
            await app.get_chat(app.LOG_CHAT)
            await app.send_message(
                app.LOG_CHAT,
                "The DeadlyUserbot is online now."
            )
        except PeerIdInvalid:
            pass

    await idle() # block execution



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
