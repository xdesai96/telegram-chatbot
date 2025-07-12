import aiohttp
from app.utils.i18n import _
from app.config import settings

async def get_weather(city: str, lang: str = settings.DEFAULT_LANG) -> str:
  if not settings.OPENWEATHER_API_KEY:
    return _("weather_no_api_key", lang=lang)

  url = "https://api.openweathermap.org/data/2.5/weather"
  params = {
    "q": city,
    "appid": settings.OPENWEATHER_API_KEY,
    "units": "metric",
    "lang": lang,
  }

  async with aiohttp.ClientSession() as session:
    async with session.get(url, params=params) as resp:
      if resp.status != 200:
        return _("weather_city_not_found", lang=lang, city=city)

      data = await resp.json()
      name = data["name"]
      country = data["sys"]["country"]
      temp = data["main"]["temp"]
      feels_like = data["main"]["feels_like"]
      humidity = data["main"]["humidity"]
      wind = data["wind"]["speed"]
      weather_desc = data["weather"][0]["description"].capitalize()

      return (
        _("weather_template", lang=lang, city=f"{name}（{country}）",
        temp=temp, feels_like=feels_like, humidity=humidity,
        wind=wind, description=weather_desc,)
      )
