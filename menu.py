import os
from handlers import TOKEN
from aiogram import Bot, Dispatcher, executor, types
import keyboards as kb
import classes as cl
from aiogram.types import InputFile

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_hello(message: types.File):
    id = message.chat.id
    await message.answer('Привет, что хочешь найти?😀', reply_markup=kb.m1)
    await bot.send_audio(chat_id=id, audio=cl.a)

@dp.message_handler()
async def process_hello(message: types.File):
    if message.text == 'Поиск по жанру':
        await message.answer('Вот доступные жанры', reply_markup=kb.m2)
    elif message.text == 'Поиск по исполнителю':
        await message.answer('Вот доступные исполнители', reply_markup=kb.m3)
    elif message.text == 'PORCHY':
        for x in range(0, 4):
            if cl.spis[x].art == 'PORCHY':
                await bot.send_audio(chat_id=id, audio=InputFile(os.path.realpath(cl.spis[x].put.get_file().name)))
            if cl.spis[x].art == 'Blaze':
                await bot.send_audio(chat_id=id, audio=InputFile(os.path.realpath(cl.spis[x].put.get_file().name)))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
