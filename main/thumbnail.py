from pyrogram import Client, filters 
from config import ADMIN, Thumbnail
import os

@Client.on_message(filters.private & filters.photo & filters.user(ADMIN))                            
async def set_tumb(bot, msg):     
    if Thumbnail is not None:        
        os.remove(Thumbnail)
    await bot.download_media(message=msg.photo.file_id, file_name=Thumbnail)                  
    return await msg.reply(f"Your permanent thumbnail is saved in dictionary ✅️ \nif you change yur server or recreate the server app to again reset your thumbnail⚠️")            


@Client.on_message(filters.private & filters.command("view") & filters.user(ADMIN))                            
async def view_tumb(bot, msg):
    if Thumbnail is not None:        
        await msg.reply_photo(photo=Thumbnail, caption="this is your current thumbnail")
    else:
        await msg.reply_text(text="you don't have any thumbnail")


@Client.on_message(filters.private & filters.command(["del", "del_thumb"]) & filters.user(ADMIN))                            
async def del_tumb(bot, msg):
    if Thumbnail is not None:       
        os.remove(Thumbnail)
        await msg.reply_text("your thumbnail was removed🚫")
    else:
        await msg.reply_text(text="you don't have any thumbnail")
