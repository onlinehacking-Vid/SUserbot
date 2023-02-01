from pyrogram.types import CallbackQuery
from pyrogram.errors import MessageNotModified





class AlertUser(object):
    def alert_user(self, func):
        async def wrapper(_, cb: CallbackQuery):
            user = cb.from_user
            if user and not (user.id == self.id or user.id in self.SudoUsersList()):
                await cb.answer(
                    f"You are not allowed to use me! make your own userbot at @TheDeadlyBots", 
                    show_alert=True
                )
            else:
                try:
                    await func(_, cb)
                except MessageNotModified:
                    pass
        return wrapper
