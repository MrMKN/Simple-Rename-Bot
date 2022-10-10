from pyrogram import Client
from config import *

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="simple-renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=100,
            plugins={"root": "main"},
            sleep_threshold=5,
        )
    async def start(self):
       await super().start()
       me = await self.get_me()       
       print(f"{me.first_name} | @{me.username} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳...⚡️")
       
    async def stop(self, *args):
      await super().stop()      
      print("Bot Restarting........")


bot = Bot()
bot.run()
