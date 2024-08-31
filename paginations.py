from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Pagination buttonlari
pagination = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⬅️", callback_data="orqaga"),
         InlineKeyboardButton(text="➡️", callback_data="oldinga")]
    ]
)
''