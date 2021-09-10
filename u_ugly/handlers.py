# Import library
from main import bot, dp
from aiogram import types
from aiogram.types import Message
from datetime import date
import random

today = date.today()
arrive = date(2021, 10, 22)
days_left = arrive - today

health = random.randint(20,101)

# set max keystrokes
keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)

# array for keyboard
array_keyboard = ['days', 'health']

# Start bot using func
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	text = f'''Привет! {message.from_user.full_name}'''

# Fuction of start bot
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    keyboard_markup.add(*(types.KeyboardButton(text) for text in array_keyboard))
    await message.answer(text='days - количество дней до возвращения\n\nhealth - сколько осталось здоровья', reply_markup=keyboard_markup)

# Fuction of start bot
@dp.message_handler(commands=['days'])
async def send_welcome(message: types.Message):
    keyboard_markup.add(*(types.KeyboardButton(text) for text in array_keyboard))
    await message.answer(text=days_left, reply_markup=keyboard_markup)

# Fuction of start bot
@dp.message_handler(commands=['health'])
async def send_welcome(message: types.Message):
    health = random.randint(20,101)
    keyboard_markup.add(*(types.KeyboardButton(text) for text in array_keyboard))
    await message.answer(text=f'{health}%', reply_markup=keyboard_markup)

