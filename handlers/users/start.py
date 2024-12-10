from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from keyboard_buttons import admin_keyboard
@dp.message(CommandStart())

async def start_command(message: Message,state:FSMContext):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name, telegram_id=telegram_id)
        await message.answer(text=f"Salom! {full_name} Botimizga xush kelibsiz! 🎉 Siz o'ziga xos, qiziqarli va esda qolarli niklar yaratmoqchimisiz? Endi bu juda oson! 💫 Shunchaki ism kiriting va biz sizga eng zo'r variantlarni taqdim etamiz. ",reply_markup=admin_keyboard.start_button)
        await state.clear()

    except:
        await message.answer(f"Salom! {full_name} Botimizga xush kelibsiz! 🎉 Siz o'ziga xos, qiziqarli va esda qolarli niklar yaratmoqchimisiz? Endi bu juda oson! 💫 Shunchaki ism kiriting va biz sizga eng zo'r variantlarni taqdim etamiz. 🚀",reply_markup=admin_keyboard.start_button)
        await state.clear()