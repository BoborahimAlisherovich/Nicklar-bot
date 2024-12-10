from aiogram.types import Message
from loader import dp
from aiogram.filters import Command
from keyboard_buttons import admin_keyboard
#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("Nik generatsiyasi: Foydalanuvchi ism kiritganda, bot bir nechta turli xil nik variantlarini yaratadi va ularni sahifalarga bo‘lib ko‘rsatadi. Har bir sahifada 10 ta nik ko‘rsatiladi va foydalanuvchi “Orqaga” yoki “Oldinga” tugmalari yordamida sahifalarni o‘zaro o‘zgartirishi mumkin.",reply_markup=admin_keyboard.start_button)

