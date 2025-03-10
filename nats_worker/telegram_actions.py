from telegram import Bot
from config import Config


async def init_bot(config : Config):
    print(config)
    print(config.TELEGRAM_TOKEN)
    bot = Bot(config.TELEGRAM_TOKEN)
    print('Bot for Telegram is initialized')
    return bot

async def bot_send_message(config : Config, bot: Bot, message: str):
    await bot.send_message(chat_id=config.CHAT_ID, text=message)