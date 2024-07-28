import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import TOKEN_API
from Handlers import actions
from Handlers import ikb_functions
from Handlers import SHOW
#чтобы хранить данные в оперативной памяти
from aiogram.fsm.storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()


async def main():
    bot = Bot(token=TOKEN_API)
    dp = Dispatcher(storage=storage)
    dp.include_router(actions.router)
    dp.include_router(ikb_functions.router)

    #await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

try:
    if __name__ == "__main__":
        asyncio.run(main())
except KeyboardInterrupt:
    print('exit')
