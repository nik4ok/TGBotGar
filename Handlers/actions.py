from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import CallbackQuery
from keyboards.inlinekeyboards import get_keyboard



router = Router()

@router.message(Command("add"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Это Бот-помошник по выводу статистики по оплате гаража",
        reply_markup = get_keyboard()
    )

# @router.callback_query()
# async def ink_handler(callback: CallbackQuery):
#     if callback.data == 'add':
#         await callback.message.answer('Напишите дату оплаты')




