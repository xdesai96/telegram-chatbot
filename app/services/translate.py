from googletrans import Translator

translator = Translator()

async def translate_text(text: str, dest_lang: str) -> str:
  try:
    result = await translator.translate(text, dest=dest_lang)
    return result.text
  except Exception as e:
    print(f"⚠️ Translate error: {e}")
    return None
