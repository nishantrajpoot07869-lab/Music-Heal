import os
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio

# 🔐 Environment variables (Render use karega)
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 🤖 Bot client
app = Client(
    "musicbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# 🔊 Voice call client
pytgcalls = PyTgCalls(app)

# ▶️ Start command
@app.on_message(filters.command("start"))
async def start(_, msg):
    await msg.reply_text("🎵 Music Bot is Alive!\nUse /play <song link or file>")

# 🎧 Play command (basic file based example)
@app.on_message(filters.command("play"))
async def play(_, msg):
    chat_id = msg.chat.id

    if len(msg.command) < 2:
        return await msg.reply_text("❌ Usage: /play <audio url or file path>")

    query = msg.text.split(None, 1)[1]

    try:
        await pytgcalls.join_group_call(
            chat_id,
            AudioPiped(query, HighQualityAudio())
        )
        await msg.reply_text("▶️ Playing Music...")
    except Exception as e:
        await msg.reply_text(f"❌ Error: {e}")

# ⏹ Stop command
@app.on_message(filters.command("stop"))
async def stop(_, msg):
    chat_id = msg.chat.id

    try:
        await pytgcalls.leave_group_call(chat_id)
        await msg.reply_text("⏹ Stopped Music")
    except Exception as e:
        await msg.reply_text(f"❌ Error: {e}")

# 🚀 Start bot
app.start()
pytgcalls.start()
print("🎵 Music Bot Started")
app.run()
