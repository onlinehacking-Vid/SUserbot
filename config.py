
""" Configuration file to get secure data we need """

import re
import os
import platform
import subprocess
import pkg_resources


_PMPERMIT_TEXT = """
Hey ! This is [Deadly-Userbot](https://t.me/DeadlyUserbot) Security System.
**You will be blocked if you spammed my owner's pm**
Currently My Owner is busy ! So Wait Until He Arrives.
And Better Not To Spam His here !
"""



# ------------------
class Configuration(object): # pylint: disable=too-few-public-methods
    """ configuration class """

# ---- important ----
    # api id of your telegram account (required)
    API_ID = os.getenv("API_ID")
    # api hash of your telegram account (required)
    API_HASH = os.getenv("API_HASH")
    # create a session using command [ python3 session.py ] or use repl.it (required)
    SESSION = os.getenv("SESSION")
    # access token of your bot, without this the bot will not work (required)
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    # database url (required)
    DB_URI = os.getenv("DATABASE_URL")
    # a group to store logs, etc (required)
    LOG_CHAT = int(os.getenv("LOG_CHAT", "-100"))

# ---- heroku ----
    # heroku api key (required -> if hosted on heroku)
    HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")
    # heroku app name (required -> if hosted on heroku)
    HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")

# ---- afk ----
    # default reason for afk plugin (optional)
    AFK_TEXT = os.getenv("AFK_TEXT", "I am busy Right Now !")

# ---- pmpermit ----
    # add True to enable pmpermit (optional)
    PMPERMIT = os.getenv("PMPERMIT", None)
    # add custom pmpermit pic (optional)
    PMPERMIT_PIC = os.getenv("PMPERMIT_PIC", "https://te.legra.ph/file/c2107cb0558d7bd2d9772.jpg")
    # add custom pmpermit warn text (optional)
    PMPERMIT_TEXT = os.getenv("PMPERMIT_TEXT", _PMPERMIT_TEXT)
    # add custom pmpermit warn limit (optional)
    PM_LIMIT = int(os.getenv("PM_LIMIT", "3"))

# ---- user ----
    # your custom name (default: telegram name)
    USER_NAME = os.getenv("USER_NAME")
    # your custom bio (default: telegram bio)
    USER_BIO = os.getenv("USER_BIO")
    # used for alive plugin (default: DeadlyUserbot logo image)
    USER_PIC = os.getenv("USER_PIC", "https://te.legra.ph/file/c2107cb0558d7bd2d9772.jpg")
    # add your telegram id if userbot fails to get your user id
    USER_ID = os.getenv("USER_ID")
    # add your username if userbot fails to get your username
    USER_USERNAME = os.getenv("USER_USERNAME")

# --- bot ----
    # provide this if bot failes to get (optional)
    BOT_BIO = os.getenv("BOT_BIO")
    # provide this if bot fails to get (optional)
    BOT_NAME = os.getenv("BOT_NAME", "Laky")
    # provide this if bot fails to get (optional)
    BOT_PIC = os.getenv("BOT_PIC")
    # provide this if bot fails to get (optional)
    BOT_USERNAME = os.getenv("BOT_USERNAME")
    # provide this if bot fails to get (optional)
    BOT_ID = os.getenv("BOT_ID")

# ---- help menu ----
    # this will be shown on 4 buttons (settings, plugins, extra, stats) as prefix and suffix
    HELP_EMOJI = os.getenv("HELP_EMOJI", "")
    # set this text to show on help menu's closed tab
    HELP_TEXT = os.getenv("HELP_TEXT", "")
    # set this to change help menu's default pic
    HELP_PIC = os.getenv("HELP_PIC", "")

# ---- spotify ----
    # spotify token for spotify now
    SPOTIFY_TOKEN = os.getenv("SPOTIFY_TOKEN")

# ---- assistant ----
    # set your assistant name, will be used in assistant tab's about section
    ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "DeadlyBot")
    # set your assistant age
    ASSISTANT_AGE = os.getenv("ASSISTANT_AGE", "20")
    # set your assistant pic
    ASSISTANT_PIC = os.getenv("ASSISTANT_PIC", "./assets/images/Laky.jpg")
    # set your assistant about text
    ASSISTANT_TEXT = os.getenv("ASSISTANT_TEXT", "")

# ---- vcbot ----
    # start the vcbot client
    VCBOT = os.getenv("VCBOT", None)
    # make vcbot public so that everyone can use
    VCBOT_ACCESS = os.getenv("VCBOT_ACCESS", None)

# ---- other ----
    # your telegraph account name (default: DeadlyUserbot)
    TL_NAME = os.getenv("TL_NAME", "Deadly Userbot")
    # thumbnail used while uploading plugins, etc. (optional)
    THUMB_PIC = os.getenv("THUMB_PIC", "./assets/images/DeadlyUserbot.jpg")
    # temporary download location (required)
    TEMP_DICT = os.getenv("TEMP_DICT", os.path.abspath(".") + "/downloads/")
    # official repo for updates
    UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/Elric-xD/project.git")
    # this is used to get your accurate time
    TIME_ZONE = os.getenv("TIME_ZONE", "Asia/Kolkata")
    # these users can use your userbot
    SUDO_USERS = [int(x) for x in os.getenv("SUDO_USERS", "").split()] # splits on spaces
    # command trigger, it works like this: .ping => result: pong !
    TRIGGER = os.getenv("TRIGGER", ".")
    # for more info visit docs.pyrogram.org, workers section
    WORKERS = int(os.getenv("WORKERS", "8"))
    # exclude official plugins from installing, give a space between plugin names
    NO_LOAD = [int(x) for x in os.getenv("NO_LOAD", "").split()] # splits on spaces




def RunShell(args: list):
    return (subprocess.run(
        args,
        stdout=subprocess.PIPE,
        shell=True
    )).stdout.decode()


def requirements():
    with open("requirements.txt", "r") as f:
        return [x for x in f.read().split("\n") if x not in ("\n", "")]


def check_requirements():
    print("Checking Packages:\n\n")
    for pkg in requirements():
        try:
            pkg_resources.require([pkg])
        except pkg_resources.DistributionNotFound as e:
            print(f"Since {e.req} is not Installed, Installing {e.req}")
            os.system(f"pip3 install {e.req}")


device = platform.uname()[0]
if (re.match(device, "Windows", re.IGNORECASE)
    or re.match(device, "Linux", re.IGNORECASE)):

    # install ffmpeg
    if re.match(device, "Windows", re.IGNORECASE):
        # permission needed in windows
        os.system("Set-ExecutionPolicy RemoteSigned -Scope CurrentUser")
        # install scoop for installing other packages
        os.system('Invoke-Expression "& {$(Invoke-RestMethod get.scoop.sh)} -RunAsAdmin"')
        # install ffmpeg through scoop
        os.system("scoop install ffmpeg")
    elif re.match(device, "Linux", re.IGNORECASE):
        # install ffmpeg through apt
        os.system("apt install ffmpeg")

    # build config class
    class Config:
        pass

    # variable counter
    count = 1

    # check if the user config file exists
    if os.path.exists("config.text"):
        print("config.text file exists: Yes\n\n")
        with open("config.text") as f:
            content = [x for x in f.read().split("\n") if x not in ("\n", "")]

        # set text file config values
        print("Setting configuration values.\n\n")
        for x in content:
            data = x.split("=")
            file_value = data[1]
            if data[1].isdigit():
                file_value = int(data[1])

            setattr(Config, data[0], file_value)
            print(f"[{count}] Added config = {data[0]} with value = {file_value}\n")
            count += 1

    # set remaining necessary config values
    print("Setting remaining configuration values\n\n")
    for attr in dir(Configuration):
        value = getattr(Configuration, attr, None)

        if attr.isupper() and not hasattr(Config, attr):
            setattr(Config, attr, value)
            print(f"[{count}] Added config = {attr} with value = {value}\n")
            count += 1

else:
    class Config(Configuration):
        pass
