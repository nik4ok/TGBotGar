from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import CallbackQuery
import openpyxl
import xlrd

router = Router()

@router.callback_query()
async def add_func(callback: CallbackQuery):
     if callback.data == 'show':
         try:
             rb = openpyxl.load_workbook("C:\\TGbotGaraj\\payments.xlsx")
         except Exception as e:
             await callback.message.reply(f"Ошибка при загрузке файла: {e}")
             return
         sheet = rb.active
         rows = []
         for row in sheet.iter_rows(values_only=True):  # Итерируем по строкам
             # Преобразуем каждую строку в строку текста
            row_values = [str(cell) if cell is not None else '' for cell in row]  # Заменяем None на пустую строку
            rows.append(', '.join(row_values))
         await callback.message.reply('\n'.join(rows))


