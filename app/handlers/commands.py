from aiogram import Router, types, Bot
from aiogram.filters import Command
import random
import time
import asyncio
import subprocess

from app.utils.validators import is_admin
from app.utils.commands import generate_help_text, parse_command
from app.utils.i18n import _
from app.services.api_client import get_weather
from app.services.translate import translate_text
from app.keyboards.dice import retry_markup
from app.keyboards.user import user_info_markup
from app.config import settings

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! 👋 Я многофункциональый чатбот. Мой разработчик @xdesai. Чтобы использовать меня тебе надо телеграм премиум и подключить меня к своему аккаунту!")

@router.business_message()
async def commands(message: types.Message, bot: Bot):
  if not message.from_user or not message.text:
    return
  conn = await bot.get_business_connection(message.business_connection_id)
  if conn.user.id != message.from_user.id:
    return
  user_lang = settings.DEFAULT_LANG
  cmd, arg = parse_command(message.text)

  # Public commands
  if cmd in [".help", ".h"]:
    help_text = f"<b>{_('help_title', lang=user_lang)}</b>\n<blockquote expandable>" + generate_help_text(
      f"{message.from_user.id}"
    ) + "</blockquote>"
    return await message.edit_text(help_text)

  if cmd in [".info", ".i"]:
    return await message.edit_text(
      _(
        "user_info",
        lang=user_lang,
        name=message.chat.full_name,
        id=message.chat.id,
      )
    )

  if cmd == ".roll":
    number = random.randint(1, 6)
    return await message.edit_text(
      _("roll_result", lang=user_lang, number=number),
      reply_markup=retry_markup("roll"),
    )

  if cmd == ".coin":
    result = (
      _("coin_heads", lang=user_lang)
      if random.choice([True, False])
      else _("coin_tails", lang=user_lang)
    )
    return await message.edit_text(result, reply_markup=retry_markup("coin"))

  if cmd in [".weather", ".w"]:
    if not arg:
      return await message.edit_text(_("weather_usage", lang=user_lang))
    weather_info = await get_weather(arg)
    return await message.edit_text(
      weather_info or _("weather_api_error", lang=user_lang)
    )

  if cmd == ".tr":
    if not arg:
      return await message.edit_text(
        _("what_language", lang=user_lang)
      )

    to_lang = arg.split()[0].strip().lower()
    reply = message.reply_to_message

    if not reply or not reply.text:
      return await message.edit_text(
        _("no_reply_text", lang=user_lang)
      )

    source_text = reply.text
    translated = await translate_text(source_text, to_lang)

    if not translated:
      return await message.edit_text(
        _("translate_error", lang=user_lang)
      )

    return await message.edit_text(
      _("translate_result", lang=user_lang, text=translated)
    )

  if cmd == ".hearts":
    HEARTS = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🤍", "🤎", "🖤"]
    sent = await message.edit_text(random.choice(HEARTS))
    for s in range(10):
      await asyncio.sleep(1)
      try:
        await sent.edit_text(random.choice(HEARTS))
      except Exception:
        break
    return

  if cmd == ".spam":
    if not arg or len(arg.split()) < 2:
      return await message.edit_text("⚠️ Usage: .spam <count> <text>")
    parts = arg.split(maxsplit=1)
    try:
      count = int(parts[0])
    except ValueError:
      return await message.edit_text("⚠️ First argument must be a number.")
    spam_text = parts[1]
    if count > 20:
      return await message.edit_text("⛔️ Max spam limit is 20.")
    for s in range(count):
      await message.reply(spam_text)
      await asyncio.sleep(0.3)
    return

  # Admin commands
  if is_admin(f"{message.from_user.id}"):
    if cmd == ".uptime":
      uptime_sec = int(time.time() - settings.START_TIME)
      days, remainder = divmod(uptime_sec, 86400)
      hours, remainder = divmod(remainder, 3600)
      minutes, seconds = divmod(remainder, 60)
      uptime_str = f"{days}d {hours}h {minutes}m {seconds}s"
      return await message.edit_text(
        _("uptime", lang=user_lang, uptime=uptime_str)
      )
    if cmd == ".ping":
      start = time.time()
      await message.edit_text("🏓")
      latency = (time.time() - start) * 1000
      return await message.edit_text(
        _("ping", lang=user_lang, latency=int(latency))
      )
    if cmd in [".terminal", ".t"]:
      if not arg:
        return await message.edit_text(_("invalid_arg_terminal", lang=user_lang))
      try:
        result = subprocess.run(
          arg,
          shell=True,
          capture_output=True,
          text=True,
          timeout=10
        )
        output = result.stdout.strip() or ""
        error = result.stderr.strip()
        response = _("_terminal_output", lang=user_lang, cmd=arg, output=output, error=error)
        return await message.edit_text(response)
      except subprocess.TimeoutExpired:
        return await message.edit_text(_("_terminal_timeout", lang=user_lang))
      except Exception as e:
        return await message.edit_text(_("_error", lang=user_lang, err=str(e)))
