from aiogram import types
from aiogram.types import ContentType

# from handlers.users.img_to_text import text_recognition
# from loader import dp, bot
#
#
# @dp.message_handler(content_types=[ContentType.PHOTO, ContentType.DOCUMENT])
# async def get_image(message: types.Message):
#     file_path = '/Users/Wolfram_3387/PycharmProjects/Kenny/data/image.png'
#     await message.photo[-1].download(destination=file_path)
#     await bot.send_photo(chat_id=message.from_user.id, photo=message.photo[-1]['file_id'])
#     text = text_recognition(file_path)
#     await message.answer(text)
