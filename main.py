import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router
import settings


async def main():
    bot = Bot(token=settings.API_KEY)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')