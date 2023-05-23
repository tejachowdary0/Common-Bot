from pyrogram import Client, filters
from helper.database import db

@Client.on_callback_query()
async def cb_handlers(c: Client, cb: "types.CallbackQuery"):
    elif cb.data == "deleteThumbnail":
        await db.set_thumbnail(cb.from_user.id, file_id=None)
        await cb.answer("❌️ __**Your Thumbnail Deleted Successfully 🗑️**__", show_alert=True)
        await cb.message.delete(True)
