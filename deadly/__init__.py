# STARTING DEADLY USERBOT
# don't change this order

from typing import Any, Dict
from config import Config
from deadly.client import app
bot = app.bot
from deadly.core.filters import gen, regex

TEMP_SETTINGS: Dict[Any, Any] = {}
TEMP_SETTINGS["PM_COUNT"] = {}
TEMP_SETTINGS["PM_LAST_MSG"] = {}
