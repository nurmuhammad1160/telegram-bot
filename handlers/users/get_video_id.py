import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_keyboard import menu

from loader import dp, db, bot
from data.config import ADMINS



@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def get_id(message: types.Message):
    video_file_id = message.video.file_id

    await message.reply(video_file_id)