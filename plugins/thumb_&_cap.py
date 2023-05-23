from pyrogram import Client, filters
from helper.database import db

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**__Use this Command to Set the Custom Caption for Your Files. For Setting Your Caption Send Caption in the Format\n`/set_caption`__\n\nFile Caption Keys\n• `{filename}` :- Replaced by the Filename.\n• `{filesize}` :- Replaced by the Filesize.\n• `{duration}` :- Replaced by the Duration of Videos.\n\nExample :- `/set_caption <b>File Name :- {filename}\n\n💾 File Size :- {filesize}\n\n⏰ Duration :- {duration}</b>`\n\n⚠️ Note :- You Can Check the Current Caption using /see_caption**")
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("__**✅ Caption Saved**__")
   
@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("__**😔 You Don't have Any Caption**__")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("__**❌️ Caption Deleted**__")
                                       
@Client.on_message(filters.private & filters.command(['see_caption']))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**--You're Caption :---**\n\n{caption}")
    else:
       await message.reply_text("__**😔 You Don't have Any Caption**__")


@Client.on_message(filters.private & filters.command(['showthumbnail']))
async def viewthumb(client, message):    
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(chat_id=message.chat.id, photo=thumb, caption="**👆🏻 This is Your Permanent Thumbnail**")
    else:
        await message.reply_text("😔 __**You Don't have Any Thumbnail**__") 
		
@Client.on_message(filters.private & filters.command(['deletethumbnail']))
async def removethumb(client, message):
    await db.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("❌️ __**Your Thumbnail Deleted Successfully 🗑️**__")
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    star = await message.reply_text("**Please Wait...**")
    await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await star.edit("✅️ __**Your Thumbnail Saved Permanently**__")

