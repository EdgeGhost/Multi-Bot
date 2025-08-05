import os
import asyncio
from aiogram import Bot,Dispatcher

from dotenv import load_dotenv,find_dotenv

from Handlers.mess_handler import user_handler_router
from Handlers.callback_handler import user_callback_router
load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

dp.include_router(user_handler_router)
dp.include_router(user_callback_router)

async def start():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start())
