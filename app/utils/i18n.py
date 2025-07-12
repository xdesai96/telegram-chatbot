import json
import os
from app.config import settings

LOCALES_DIR = os.path.join(os.path.dirname(__file__), "../locales")
CACHE = {}


def load_locale(lang: str):
    if lang in CACHE:
        return CACHE[lang]
    try:
        path = os.path.join(LOCALES_DIR, f"{lang}.json")
        with open(path, "r", encoding="utf-8") as f:
            CACHE[lang] = json.load(f)
        return CACHE[lang]
    except FileNotFoundError:
        raise ValueError(f"Locale '{lang}' not found")


def _(key: str, lang: str = None, **kwargs):
    lang = lang or settings.DEFAULT_LANG
    strings = load_locale(lang)
    template = strings.get(key, key)
    return template.format(**kwargs)
