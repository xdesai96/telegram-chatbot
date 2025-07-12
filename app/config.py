from dotenv import load_dotenv
import os
import time

load_dotenv()


class Settings:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    START_TIME = time.time()
    ADMINS = os.getenv("ADMINS")
    DEFAULT_LANG = os.getenv("DEFAULT_LANG", "en")


settings = Settings()
