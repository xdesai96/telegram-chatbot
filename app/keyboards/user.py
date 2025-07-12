from aiogram import types
from app.utils.i18n import _
from app.config import settings

# TODO markup for userinfo

def user_info_markup(id: int = None):
  return types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text=_(f"", lang=settings.DEFAULT_LANG), callback_data=f"retry_{dice_type}")]
    ]
  )
