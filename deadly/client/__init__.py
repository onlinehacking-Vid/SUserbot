import os

try:
    import uvloop
    uvloop.install()
except ImportError:
    print("uvloop wasn't installed, userbot will work slow.")

from .bot import Bot
from .userbot import SuperClient



bot = Bot()
app = SuperClient()
