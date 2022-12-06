from aiogram import types
from loader import dp
from googletrans import Translator


@dp.message_handler()
async def translate(message: types.Message):
    translator = Translator()
    translated = translator.translate(text=message.text, dest='en')
    await message.answer(translated.text)
