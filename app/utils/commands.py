from app.utils.validators import is_admin
from app.utils.i18n import _
from app.config import settings

user_lang = settings.DEFAULT_LANG

user_commands = {
    ".help (.h)": _('_doc_help', lang=user_lang),
    ".info (.i)": _('_doc_info', lang=user_lang),
    ".roll": _('_doc_roll', lang=user_lang),
    ".coin": _('_doc_coin', lang=user_lang),
    ".weather (.w)": _('_doc_weather', lang=user_lang),
    ".tr": _('_doc_tr', lang=user_lang),
    ".hearts": _('_doc_hearts', lang=user_lang),
    ".spam": _('_doc_spam', lang=user_lang),
}

admin_commands = {
    ".ping": _('_doc_ping', lang=user_lang),
    ".uptime": _('_doc_uptime', lang=user_lang),
    ".terminal (.t)": _('_doc_terminal', lang=user_lang)
}


def generate_help_text(user_id: str) -> str:
    cmds = user_commands.copy()
    if is_admin(user_id):
        cmds.update(admin_commands)
    return "\n".join(f"<code>{cmd}</code> — <b>{desc}</b>" for cmd, desc in cmds.items())


def parse_command(text: str):
    parts = text.strip().split(maxsplit=1)
    cmd = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else None
    return cmd, arg
