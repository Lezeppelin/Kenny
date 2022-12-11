from aiogram import types

from filters.all_filters import IsPrivate
from loader import dp
from googletrans import Translator


@dp.message_handler(IsPrivate())
async def translate_private(message: types.Message):
    translator = Translator()
    translated = translator.translate(text=message.text, dest='en')
    await message.answer(translated.text)


@dp.message_handler()
async def translate_group(message: types.Message):
    translator = Translator()
    translated = translator.translate(text=message.text, dest='en')
    await message.answer(translated.text)
