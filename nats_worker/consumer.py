import asyncio
import os
from telegram import Bot
from faststream.nats import NatsBroker
from dotenv import load_dotenv

load_dotenv("deploy.env")

NATS_URL = os.getenv("NATS_URL", "nats://nats:4222")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

broker = NatsBroker(NATS_URL)

async def init_bot():
    bot = Bot(TELEGRAM_TOKEN)
    print('Bot for Telegram is initialized')
    return bot

async def bot_send_message(bot: Bot, message: str):
    await bot.send_message(chat_id=CHAT_ID, text=message)

@broker.subscriber("new.customer")
async def process_message(message: dict):
    print(f"Received message: {message}")
    bot = await init_bot()
    #await bot_send_message(bot, f"New customer: {message}")

async def main():
    await broker.start()
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())