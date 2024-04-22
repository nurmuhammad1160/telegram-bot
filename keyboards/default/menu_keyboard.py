import logging

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData

from loader import db


async def categories_keyboard():

    markup = ReplyKeyboardMarkup(row_width=2)

    categories = await db.get_categories()

    for category in categories:
        # Kategoriyaga tegishli mahsulotlar sonini topamiz
        number_of_items = await db.count_products(category["category_name"])


        button_text = f"{category['category_name']}"

        markup.insert(
            KeyboardButton(text=button_text)
        )

    return markup


async def subcategories_keyboard(category):
    markup = ReplyKeyboardMarkup(row_width=2)


    subcategories = await db.get_subcategories(category)

    for subcategory in subcategories:
        # Kategoriyada nechta mahsulot borligini tekshiramiz
        number_of_items = await db.count_products(
            category_name=category, subcategory_name=subcategory["subcategory_name"]
        )

        button_text = f"{subcategory['subcategory_name']}"

    return markup


async def items_keyboard(category, subcategory):

    markup = ReplyKeyboardMarkup(row_width=2)

    items = await db.get_products(category, subcategory)
    for item in items:
        # Tugma matnini yasaymiz
        button_text = f"{item['lesson_name']}"

        



