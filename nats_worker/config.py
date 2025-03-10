import os

class Config:
    def __init__(self):
        self.NATS_URL = os.getenv("NATS_URL", "nats://nats:4222")
        self.TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
        self.CHAT_ID = os.getenv("CHAT_ID")