import re
from telegram import Bot
from telegram.constants import ParseMode
from config import Config
from lexicon import rus


def escape_markdown_v2(text: str) -> str:
    # Define a list of characters that need to be escaped in MarkdownV2
    dangerous_characters = r"([*_`\[\]()~>#+\-=|{}.!])"
    return re.sub(dangerous_characters, r"\\\1", text)


async def init_bot(config: Config):
    print(config)
    print(config.TELEGRAM_TOKEN)
    bot = Bot(config.TELEGRAM_TOKEN)
    print("Bot for Telegram is initialized")
    return bot


def format_the_message(message: dict) -> str:
    formatted_message = rus["new_order"].format(**message)
    return escape_markdown_v2(formatted_message)


async def bot_send_message(config: Config, bot: Bot, message: str):
    await bot.send_message(
        chat_id=config.CHAT_ID,
        text=message,
        parse_mode=ParseMode.MARKDOWN_V2
    )
