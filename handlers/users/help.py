from aiogram.types import Message
from loader import dp
from aiogram.filters import Command
from keyboard_buttons import admin_keyboard

#help commands
@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("Yordam kerakmi? Biz sizga o'zingizga mos, noyob va original nik yaratishda yordam beramiz! 🔥 Istalgancha nik giniratsiya qiling, tanlang va boshqa hech kimga o'xshamaydigan uslubingizni yarating! 😎",reply_markup=admin_keyboard.start_button)
