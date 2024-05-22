from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn = [
    [KeyboardButton(text="Chat users"), KeyboardButton(text="Bot users")]
]
keyboard = ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True)