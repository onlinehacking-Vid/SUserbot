
# Copyright (c) 2023 team-Deadly
# Part of: DeadlyUserbot

import os
import asyncio

from pyrogram.types import Message
from deadly import app, gen



app.CMD_HELP.update(
    {"hack" : (
        "hack",
        {
        "hack" : " To perform a hack prank to users",        
        }
        )
    }
)




@app.on_message(gen(["hack", "heck"]))
async def heck_dat(_, message: Message):
    r_msg = message.reply_to_message
    heck_msg = await app.send_edit("**[root@deadlyuserbot]** `enable tg-hacker && clear`")
    if not r_msg:
        return await heck_msg.edit("`⚠ Reply to a telegram user to perform a hack!`")
    if not r_msg.from_user:
        return await heck_msg.edit("`⚠ Reply to a telegram user to perform a hack!`")
    # User info
    user_id = r_msg.from_user.id
    user_mention = r_msg.from_user.mention
    user_dc = r_msg.from_user.dc_id
    # Hack animation characters (stage 1)
    stage1_msg = ""
    hack_animation_stage1_chars = [
        "**[root@deadlyuserbot]** `tg-hacker init` \n",
        "`>> Initializing telegram hacker...` \n\n",
        "**[root@deadlyuserbot]** `tg-hacker --check-tools` \n",
        "`>> Checking if the required tools are installed...` \n",
        "`>> Done Checking! All the tools are installed!` \n\n",
        f"**[root@deadlyuserbot]** `mkdir {user_id}` \n",
        f"`>> Creating Directory for the user...` \n",
        "`>> Successfully Created the Directory!` \n\n",
        f"**[root@deadlyuserbot]** `cd {user_id} && tg-hacker --set-config-user-path pwd && cd` \n",
        f"\n`Forwarding the process to stage 2`"
    ]
    # Hack animation characters (stage 2)
    stage2_msg = ""
    hack_animation_stage2_chars = [
        "**[root@deadlyuserbot]** `tg-hacker --connect-to-server --most-stable` \n",
        "`>> Connecting to the telegram servers...` \n"
        "`>> Connected ✓` \n\n",
        "**[root@deadlyuserbot]** `tg-hacker --collect-user-info --less-verbose` \n"
        f"`>> Extracting the information about user id - {user_id}` \n",
        f"`>> Process completed ✓. Collected information about` {user_mention} . \n"
        "\n`Forwarding the process to stage 3`"
    ]
    # Hack animation characters (stage 3)
    stage3_msg = ""
    hack_animation_stage3_progress = [
        "`▱▱▱▱▱▱▱▱▱▱▱▱▱ 0%` \n",
        "`▰▱▱▱▱▱▱▱▱▱▱▱▱ 5%` \n",
        "`▰▱▱▱▱▱▱▱▱▱▱▱▱ 14%` \n",
        "`▰▰▱▱▱▱▱▱▱▱▱▱▱ 23%`\n",
        "`▰▰▰▰▱▱▱▱▱▱▱▱▱ 31%` \n",
        "`▰▰▰▰▰▱▱▱▱▱▱▱▱ 43%` \n",
        "`▰▰▰▰▰▰▰▱▱▱▱▱▱ 59%` \n",
        "`▰▰▰▰▰▰▰▰▱▱▱▱▱ 65%` \n",
        "`▰▰▰▰▰▰▰▰▰▰▱▱▱ 78%` \n",
        "`▰▰▰▰▰▰▰▰▰▰▰▱▱ 89%` \n",
        "`▰▰▰▰▰▰▰▰▰▰▰▰▱ 94%` \n",
        "`▰▰▰▰▰▰▰▰▰▰▰▰▰ 100%` \n"
    ]
    hack_animation_stage3_chars = [
        "**[root@deadlyuserbot]** `tg-hacker start --use-tg-brut --less-verbose --auto-cmd` \n",
        "`>> Starting the hack...` \n",
        "`>> Downloading Telegram-Bruteforce-8.3.2.tar.gz (1.9MiB)` \n"
        "`>> Download Completed ✓` \n\n",
        "**[root@deadlyuserbot]** `tg-hacker --check-config` \n",
        "`>> Checking user config file...` \n"
        f"`>> Found config file - {user_id}.conf` \n",
        "**[root@deadlyuserbot]** `tg-hacker --upload` \n",
        f"`>> Uploading the hacked accound details to telegram server - ID {user_dc if user_dc else 'Main'}` \n\n",
    ]
    # Hack animation characters (stage 4)
    stage4_msg = ""
    hack_animation_stage4_chars = [
        "**[root@deadlyuserbot]** `tg-hacker check-if-completed` \n",
        "`>> Checking...` \n"
        "`>> Hacking completed ✓` \n\n",
        "**[root@deadlyuserbot]** `tg-hacker show --fix-for-tg-msg` \n\n\n",
        f"**Dear {user_mention}, Your telegram account has been hacked by me ☠! \nYou have to pay at least $10 to fix your telegram account!**"
    ]
    # Editing the message (stage 1)
    for char1 in hack_animation_stage1_chars:
        await asyncio.sleep(1)
        stage1_msg += char1
        await heck_msg.edit(stage1_msg)
    await asyncio.sleep(3)
    # Editing the message (stage 2)
    await heck_msg.edit(f"{stage1_msg} \n\n**[root@deadlyuserbot]** `clear`")
    for char2 in hack_animation_stage2_chars:
        await asyncio.sleep(2)
        stage2_msg += char2
        await heck_msg.edit(stage2_msg)
    await asyncio.sleep(4)
    # Editing the message (stage 3)
    await heck_msg.edit(f"{stage2_msg} \n\n**[root@deadlyuserbot]** `clear && tg-hacker --set-stage stage3`")
    for char3 in hack_animation_stage3_chars:
        await asyncio.sleep(3)
        stage3_msg += char3
        await heck_msg.edit(stage3_msg)
    await asyncio.sleep(3)
    for prgs in hack_animation_stage3_progress:
        await asyncio.sleep(3) 
        actual_prgs_msg = stage3_msg + prgs
        await heck_msg.edit(actual_prgs_msg)
    await asyncio.sleep(4)
    # Editing the message (stage 4)
    await heck_msg.edit(f"{actual_prgs_msg} \n**[root@deadlyuserbot]** `clear && tg-hacker --set-stage stage4`")
    for char4 in hack_animation_stage4_chars:
        await asyncio.sleep(3)
        stage4_msg += char4
        await heck_msg.edit(stage4_msg)
