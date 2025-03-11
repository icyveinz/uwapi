from telegram import Bot
from telegram.constants import ParseMode
from config import Config
from lexicon import rus


async def init_bot(config: Config):
    print(config)
    print(config.TELEGRAM_TOKEN)
    bot = Bot(config.TELEGRAM_TOKEN)
    print("Bot for Telegram is initialized")
    return bot


def format_the_message(message: dict) -> str:
    return rus["new_order"].format(**message)


async def bot_send_message(config: Config, bot: Bot, message: str):
    await bot.send_message(
        chat_id=config.CHAT_ID, text=message, parse_mode=ParseMode.MARKDOWN_V2
    )
