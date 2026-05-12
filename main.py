from pyrogram import Client

bot = Client(
    "musicbot",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

@bot.on_message()
def start(client, message):
    message.reply_text("🎵 Music Bot is Running!")

bot.run()
