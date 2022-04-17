import asyncio
from telethon import TelegramClient, events
import curses


# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.

async def main():
  client = TelegramClient('main_session', api_id, api_hash)
  await client.start()

asyncio.run(main())