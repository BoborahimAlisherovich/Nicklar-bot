from aiogram.types import Message
from loader import dp, db
from aiogram.filters import Command
import json

def load_texts():
    with open("languages.json", "r", encoding="utf-8") as f:
        return json.load(f)

texts = load_texts()

@dp.message(Command("help"))
async def help_commands(message: Message):
    telegram_id = message.from_user.id

    user = db.select_user_by_id(telegram_id=telegram_id)

    language = "uz" 

    if user:
        language = user[2]
    text = texts.get(language, {}).get("help", "Tilga mos matn topilmadi.")

    await message.answer(text, parse_mode='html')

    