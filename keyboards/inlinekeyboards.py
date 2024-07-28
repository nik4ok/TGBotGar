from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup

def get_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(text = "Добавить оплату", callback_data='add'),
            InlineKeyboardButton(text = "Удалить оплату", callback_data='del')
        ],
         [
             InlineKeyboardButton(text = 'Показать список оплат', callback_data='show'),
             InlineKeyboardButton(text = 'Подсчитать все выплаты', callback_data='count')
          ],
    ]
    ikb = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return ikb


