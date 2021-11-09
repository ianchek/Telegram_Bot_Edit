from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton('Поиск по исполнителю')
b2 = KeyboardButton('Поиск по названию')
b3 = KeyboardButton('Поиск по жанру')

Hip = KeyboardButton('Hip-hop')
Rap = KeyboardButton('Rap')
Pop = KeyboardButton('Pop')

PORCHY = KeyboardButton('PORCHY')
Blaze = KeyboardButton('Blaze')

m1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(b1).row(b2).row(b3)
m2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(Hip).row(Rap).row(Pop)
m3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(PORCHY).row(Blaze)