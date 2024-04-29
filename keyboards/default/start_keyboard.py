from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Darslarni boshlash"),
        ],
    ],
    resize_keyboard=True,
)
