import logging

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor

API_TOKEN = '1984080956:AAEcKOHcClxGY3sMxRYm3QizwoolWegd6m4'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    firstname = State()
    lastname = State()
    group = State()
    startedu = State()

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await Form.firstname.set()
    await message.reply("Hello, what is your name?")

@dp.message_handler(state=Form.firstname)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['firstname'] = message.text
    await Form.next()
    await message.reply("What is your last name?")

@dp.message_handler(state=Form.lastname)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['lastname'] = message.text
    await Form.next()
    await message.reply("What group do you study in?")

@dp.message_handler(lambda message: message.text, state=Form.group)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await Form.next()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("2017", "2018", "2019", "2020")
    
    await message.reply("What is your last name?", reply_markup=markup)
    
@dp.message_handler(lambda message: message.text not in ["2017", "2018", "2019", "2020"], state=Form.startedu)
async def process_gender_invalid(message: types.Message):
        return await message.reply("Wrong answer. Choose the answer on your keyboard.")

@dp.message_handler(state=Form.startedu)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['startedu'] = message.text
    
        markup = types.ReplyKeyboardRemove()

        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Nice to meet you!,', md.bold(data['firstname'] + ' ' + data['lastname'])),
                md.text('Your group:', data['group']),
                md.text('Started studying in :', data['startedu']),
                sep='\n',
            ),
            reply_markup=markup,
            parse_mode=ParseMode.MARKDOWN,
        )
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
