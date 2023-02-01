import time
import logging
import platform

import pyrogram
from requests.exceptions import ConnectionError
from config import Config
from telegraph import Telegraph
from pyrogram import __version__ as pyrogram_version
from deadly.database import Database
from deadly.core.helpers import Helpers
from deadly.core.fastpyro import Methods






class ClassManager(Config, Helpers, Database, Methods):
    # versions /
    python_version = str(platform.python_version())
    pyrogram_version = str(pyrogram_version)

    # assistant /
    assistant_name = "Laky"
    assistant_version = "v.1.0.0"

    # userbot /
    userbot_name = "deadly"
    userbot_version = "v.2.0.0"  # as telethon alrdy launched
    # containers /
    CMD_HELP = {}

    # owner details /
    owner_name = "【𓆩𝘽𝙇𝘼𝙕𝙀 ✘ 𝙊𝙋𓆪】⛓️ᥫʀ᭡"
    owner_id = 5937170640
    owner_username = "@Elric_xD"

    # other /
    message_ids = {}
    PIC = "https://te.legra.ph/file/99d2c1e7570d241a67207.mp4"
    Repo = "https://github.com/Team-Deadly/Userbot.git"
    StartTime = time.time()
    utube_object = object
    callback_user = None
    whisper_ids = {}

    # debugging /


    logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)
    logging.getLogger("pyrogram.session.session").setLevel(logging.WARNING)
    logging.getLogger("pyrogram.session.internals.msg_id").setLevel(logging.WARNING)
    logging.getLogger("pyrogram.dispatcher").setLevel(logging.WARNING)
    logging.getLogger("pyrogram.connection.connection").setLevel(logging.WARNING)
    log = logging.getLogger()

    # telegraph /
    try:
        telegraph = Telegraph()
        telegraph.create_account(short_name=Config.TL_NAME or "Team-Deadly")
    except ConnectionError:
        telegraph = None
