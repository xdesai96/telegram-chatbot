from app.bot import dp, bot
import asyncio

async def main():
    from app.handlers import commands, callback

    dp.include_routers(commands.router, callback.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
