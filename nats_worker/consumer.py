import asyncio
from faststream.nats import NatsBroker
from dotenv import load_dotenv
from config import Config
from telegram_actions import format_the_message, init_bot, bot_send_message

load_dotenv("deploy.env")

config = Config()

broker = NatsBroker(config.NATS_URL)


@broker.subscriber("new.customer")
async def process_message(message: dict):
    print(f"Received message: {message}")
    bot = await init_bot(config)
    await bot_send_message(config, bot, format_the_message(message))


async def main():
    await broker.start()
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
