import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router



async def main():
    bot = Bot(token='7889002966:AAEUIN8Y5F3u4rAENWYfHdga29xzdZBmC9w')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')