from pyrogram import Client, filters, idle
from asyncio import get_event_loop
from cxxfilt import demangle

BOT_TOKEN = ""


app = Client(":memory:", bot_token=BOT_TOKEN, api_id=6, api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e")

@app.on_message(filters.command("demangle"))
async def hoe(_, m):
    arg = m.text.split(None, 1)[1].strip()
    await m.reply(f"`{demangle(arg)}`", parse_mode="markdown")

async def main():
    await app.start()
    await idle()

loop = get_event_loop()
loop.run_until_complete(main())

