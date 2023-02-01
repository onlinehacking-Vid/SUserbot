

from pyrogram import Client, enums, filters
from pyrogram.types import Message
from sqlalchemy.exc import IntegrityError


from deadly import TEMP_SETTINGS, app, gen
from deadly.core.basic import edit_or_reply
from deadly.core.tools import get_arg

BLAZE = "5937170640"
DEF_UNAPPROVED_MSG = (
    "╔════════════════════╗\n"
    "  ⛑ 𝗔𝗧𝗧𝗘𝗡𝗧𝗜𝗢𝗡 𝗣𝗟𝗘𝗔𝗦𝗘 ⛑  \n"
    "╚════════════════════╝\n"
    "• I haven't approved you for PM.\n"
    "• Wait until I approve your PM.\n"
    "• Don't Spam in Chat or you will be automatically banned.\n"
    "╔════════════════════╗\n"
    " 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 - [𝗗𝗲𝗮𝗱𝗹𝘆𝗨𝘀𝗲𝗿𝗯𝗼𝘁](https://t.me/DeadlyUserbot)  \n"
    "╚════════════════════╝\n"
)

app.CMD_HELP.update(
    {"pmpermit" : (
        "pmpermit",
        {
        "approve" : "reply to user to approve them in pm.",
        "disapprove" : "reply to user to disapprove them in pm."
        }
        )
    }
)

@app.on_message(
    ~filters.me & filters.private & ~filters.bot & filters.incoming, group=69
)
async def incomingpm(client: Client, message: Message):
    try:       
        from deadly.database.postgres.pmpermit_sql import is_approved
    except BaseException:
        pass

    if await auto_accept(client, message):
        message.continue_propagation()
    if message.chat.id != 777000:
        PM_LIMIT = 5
        getmsg = DEF_UNAPPROVED_MSG
        if getmsg is not None:
            UNAPPROVED_MSG = getmsg
        else:
            UNAPPROVED_MSG = DEF_UNAPPROVED_MSG

        apprv = is_approved(message.chat.id)
        if not apprv and message.text != UNAPPROVED_MSG:
            if message.chat.id in TEMP_SETTINGS["PM_LAST_MSG"]:
                prevmsg = TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id]
                if message.text != prevmsg:
                    async for message in client.search_messages(
                        message.chat.id,
                        from_user="me",
                        limit=10,
                        query=UNAPPROVED_MSG,
                    ):
                        await message.delete()
                    if TEMP_SETTINGS["PM_COUNT"][message.chat.id] < (int(PM_LIMIT) - 1):
                        ret = await message.reply_text(UNAPPROVED_MSG)
                        TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id] = ret.text
            else:
                ret = await app.send_edit(UNAPPROVED_MSG)
                if ret.text:
                    TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id] = ret.text
            if message.chat.id not in TEMP_SETTINGS["PM_COUNT"]:
                TEMP_SETTINGS["PM_COUNT"][message.chat.id] = 1
            else:
                TEMP_SETTINGS["PM_COUNT"][message.chat.id] = (
                    TEMP_SETTINGS["PM_COUNT"][message.chat.id] + 1
                )
            if TEMP_SETTINGS["PM_COUNT"][message.chat.id] > (int(PM_LIMIT) - 1):
                await message.reply("**Sorry you have been blocked because of spamming in chat**")
                try:
                    del TEMP_SETTINGS["PM_COUNT"][message.chat.id]
                    del TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id]
                except BaseException:
                    pass

                await client.block_user(message.chat.id)

    message.continue_propagation()


async def auto_accept(client, message):
    try:
        from deadly.database.postgres.pmpermit_sql import approve, is_approved
    except BaseException:
        pass

    if message.chat.id not in [client.me.id, 777000]:
        if is_approved(message.chat.id):
            return True

        async for msg in client.get_chat_history(message.chat.id, limit=1):
            if msg.from_user.id == client.me.id:
                try:
                    del TEMP_SETTINGS["PM_COUNT"][message.chat.id]
                    del TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id]
                except BaseException:
                    pass

                try:
                    approve(chat.id)
                    async for message in client.search_messages(
                        message.chat.id,
                        from_user="me",
                        limit=10,
                        query=UNAPPROVED_MSG,
                    ):
                        await message.delete()
                    return True
                except BaseException:
                    pass

    return False


@app.on_message(gen(["a", "approve"]), group=0)
async def approvepm(client: Client, message: Message):
    try:
        from deadly.database.postgres.pmpermit_sql  import approve
    except BaseException:
        await message.edit("Running on Non-SQL mode!")
        return

    if message.reply_to_message:
        reply = message.reply_to_message
        replied_user = reply.from_user
        if replied_user.is_self:
            await message.edit("You can't approve yourself.")
            return
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        uid = replied_user.id
    else:
        aname = message.chat
        if not aname.type == enums.ChatType.PRIVATE:
            await message.edit(
                "You're not currently in PM and you haven't replied to someone's message."
            )
            return
        name0 = aname.first_name
        uid = aname.id

    try:
        approve(uid)
        await message.edit(f"**Receive Messages From** [{name0}](tg://user?id={uid})!")
    except IntegrityError:
        await message.edit(
            f"[{name0}](tg://user?id={uid}) probably already approved for PM."
        )
        return


@app.on_message(gen(["da", "disapprove"]), group=0)
async def disapprovepm(client: Client, message: Message):
    try:
        from deadly.database.postgres.pmpermit_sql  import dissprove
    except BaseException:
        await message.edit("Running on Non-SQL mode!")
        return

    if message.reply_to_message:
        reply = message.reply_to_message
        replied_user = reply.from_user
        if replied_user.is_self:
            await message.edit("You can't deny yourself.")
            return
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        uid = replied_user.id
    else:
        aname = message.chat
        if not aname.type == enums.ChatType.PRIVATE:
            await message.edit(
                "You're not currently in PM and you haven't replied to someone's message."
            )
            return
        name0 = aname.first_name
        uid = aname.id

    dissprove(uid)

    await message.edit(
        f"**Message** [{name0}](tg://user?id={uid}) **Rejected, Please Don't Spam Chat!**"
    )
    
