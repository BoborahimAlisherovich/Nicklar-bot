import json
from aiogram.types import Message, CallbackQuery
from loader import dp, db
from aiogram.filters import CommandStart
from keyboard_buttons.admin_keyboard import create_menu_buttons, language
from aiogram.fsm.context import FSMContext

# JSON matnlarini yuklash
def load_texts():
    with open("languages.json", "r", encoding="utf-8") as f:
        return json.load(f)

texts = load_texts()

# /start komanda uchun handler
# /start komanda uchun handler
@dp.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    # State tozalash
    await state.clear()

    # Foydalanuvchi ma'lumotlarini olish
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id

    # Foydalanuvchini ma'lumotlar bazasidan tekshirish
    user = db.select_user_by_id(telegram_id=telegram_id)
    if user:
        # Agar foydalanuvchi bazada mavjud bo'lsa
        selected_language = user[2]  # Ma'lumotlar bazasidagi til
        await message.answer(
            text=texts[selected_language]["welcome_message"].format(full_name=full_name),
            parse_mode='html',
            reply_markup=create_menu_buttons(selected_language)
        )
    else:
        # Foydalanuvchini bazaga qo'shish
        db.add_user(full_name=full_name, telegram_id=telegram_id, language="uz")

        # Boshlang'ich xabarni yuborish
        await message.answer(
            text=texts["uz"]["start_message"], 
            parse_mode="html",
            reply_markup=language
        )
        
# Til tanlash tugmasi uchun callback handler
@dp.callback_query(lambda c: c.data in ["uz", "us", "ru"])
async def edit(callback: CallbackQuery, state: FSMContext):
    # State tozalash
    await state.clear()

    # Callback xabarini o'chirish
    await callback.message.delete()

    # Tanlangan tilni olish
    selected_language = callback.data
    full_name = callback.from_user.full_name
    telegram_id = callback.from_user.id

    # Foydalanuvchi ma'lumotlarini yangilash
    user = db.select_user_by_id(telegram_id=telegram_id)
    if user is None:
        db.add_user(full_name=full_name, telegram_id=telegram_id, language=selected_language)
    else:
        db.update_user_language(telegram_id=telegram_id, language=selected_language)

    # Tanlangan til haqida xabar yuborish
    await callback.message.answer(texts[selected_language]["selected_language"])

    # Foydalanuvchini kutib olish xabarini yuborish
    await callback.message.answer(
        text=texts[selected_language]["welcome_message"].format(full_name=full_name),
        parse_mode='html',
        reply_markup=create_menu_buttons(selected_language)
    )

# Tilni o'zgartirish xabari uchun tekshiruvchi funksiya
def language_message(message_text):
    possible_texts = [
        texts.get(lang, {}).get("menu", {}).get("menu_button_5", "")
        for lang in texts
    ]
    return message_text in possible_texts

# Tilni o'zgartirish uchun handler
@dp.message(lambda message: language_message(message.text))
async def language_us(message: Message, state: FSMContext):
    # State tozalash
    await state.clear()

    # Foydalanuvchi ma'lumotlarini olish
    telegram_id = message.from_user.id
    user = db.select_user_by_id(telegram_id=telegram_id)

    language_u = "uz"
    if user:
        language_u = user[2]  # Ma'lumotlar bazasidagi til

    # Xabar yuborish
    text = texts.get(language_u, {}).get("start_message", "Tilga mos matn topilmadi.")
    await message.answer(text, parse_mode='html', reply_markup=language)

