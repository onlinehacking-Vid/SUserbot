from deadly.client import app

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@app.bot.on_message(filters.command("quote"), group=-1)
async def bot_anime_quotes(_, m):
    await app.bot.send_message(
        m.chat.id,
        app.quote(),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "More", callback_data="animequote-tab"
                    )
                ],
            ]
        )
    )
