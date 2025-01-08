from aiogram.types import Message
from loader import dp,db
from aiogram.filters import Command
from keyboard_buttons import admin_keyboard
# @dp.message(Command("about"))
# async def about_commands(message:Message):
#     await message.answer("Nik generatsiyasi: Foydalanuvchi ism kiritganda, bot bir nechta turli xil nik variantlarini yaratadi va ularni sahifalarga bo‘lib ko‘rsatadi. Har bir sahifada 10 ta nik ko‘rsatiladi va foydalanuvchi “Orqaga” yoki “Oldinga” tugmalari yordamida sahifalarni o‘zaro o‘zgartirishi mumkin.",reply_markup=admin_keyboard.start_button)


# from aiogram.fsm.context import FSMContext
import json



def load_texts():
    with open("languages.json", "r", encoding="utf-8") as f:
        return json.load(f)

texts = load_texts()

@dp.message(Command("about"))
async def help_commands(message: Message):
    telegram_id = message.from_user.id

    user = db.select_user_by_id(telegram_id=telegram_id)

    language = "uz" 

    if user:
        language = user[2]
    text = texts.get(language, {}).get("about", "Tilga mos matn topilmadi.")

    await message.answer(text, parse_mode='html')

    