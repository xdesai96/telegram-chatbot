import random
from aiogram import Router, types, exceptions
from app.keyboards.dice import retry_markup
from app.utils.i18n import _
from app.config import settings

router = Router()
user_lang = settings.DEFAULT_LANG


@router.callback_query()
async def callback_handler(callback_query: types.CallbackQuery):
  if callback_query.message.from_user.id != callback_query.from_user.id:
    return await callback_query.answer(f"{_('not_allowed', lang=user_lang)}")

  if callback_query.data.startswith("retry_"):
    dice_type = callback_query.data.removeprefix("retry_").strip()

    if dice_type == "roll":
      new_number = random.randint(1, 6)
      text = (
        '<tg-emoji emoji-id="5298938093536044655">🎲</tg-emoji> '
        f'Выпало число: {new_number}'
      )

    elif dice_type == "coin":
      result = (
        _("coin_heads", lang=user_lang)
        if random.choice([True, False])
        else _("coin_tails", lang=user_lang)
      )
      text = result

    else:
      return await callback_query.answer(_("unknown_retry", lang=user_lang))

    try:
      await callback_query.message.edit_text(
        text,
        reply_markup=retry_markup(dice_type),
      )
      return await callback_query.answer()
    except exceptions.TelegramBadRequest:
      return await callback_query.answer()

  return await callback_query.answer(_("invalid_callback", lang=user_lang))
