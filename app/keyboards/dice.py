from aiogram import types
from app.utils.i18n import _
from app.config import settings


def retry_markup(dice_type: str = None):
  return types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text=_(f"retry_{dice_type}", lang=settings.DEFAULT_LANG), callback_data=f"retry_{dice_type}")]
    ]
  )
