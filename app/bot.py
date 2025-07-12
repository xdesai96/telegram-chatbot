from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from app.config import settings
from aiogram.enums import parse_mode

bot = Bot(
    token=settings.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=parse_mode.ParseMode.HTML),
)
dp = Dispatcher()
