import os


class Config:
    def __init__(self):
        self.SENTRY_DSN = os.getenv("SENTRY_DSN")
        self.DJANGO_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
        self.DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")
