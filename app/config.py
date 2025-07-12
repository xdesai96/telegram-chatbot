from dotenv import load_dotenv
import os
import time

load_dotenv()


class Settings:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    START_TIME = time.time()
    ADMINS = os.getenv("ADMINS")
    COMMAND_COOLDOWNS = {
        ".help": 5,
        ".info": 5,
        ".roll": 3,
        ".coin": 3,
        ".weather": 10,
        ".ping": 2,
        ".uptime": 5,
    }
    DEFAULT_LANG = os.getenv("DEFAULT_LANG", "en")


settings = Settings()
