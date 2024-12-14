from aiogram.types import Message
from loader import dp, bot, ADMINS
from aiogram.fsm.context import FSMContext
from states.bulimlar import AdminStates
from aiogram.types import CallbackQuery, ContentType
from keyboard_buttons import admin_keyboard
from aiogram import types
from aiogram import F
import logging
from aiogram.utils.keyboard import InlineKeyboardBuilder
import re

# Logger sozlamalari
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Orqaga qaytish handler
@dp.message(F.text == "♻️ Orqaga")
async def orqaga(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Bosh menyuga qaytdingiz. Ism kriting yoki kerakli bo'limlarni tanlang", 
        reply_markup=admin_keyboard.start_button
    )

# Inline keyboard yaratish
def create_inline_keyboard(user_id):
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text="Javob berish", callback_data=f"reply:{user_id}"
    )
    return keyboard_builder.as_markup()

# Telegram user_link yaratish
def get_user_link(user_id, first_name):
    """
    Foydalanuvchining bosiladigan profil linkini qaytaradi.
    """
    return f"[{first_name}](tg://user?id={user_id})"

# Admin xabar yuborish
@dp.message(F.text == "👨‍💼Admin")
async def admin_message(message: Message, state: FSMContext):
    await message.answer(
        "Admin uchun xabar yuboring:", reply_markup=admin_keyboard.orqaga_button
    )
    await state.set_state(AdminStates.waiting_for_admin_message)

# Admin xabarini qabul qilish va yuborish
@dp.message(AdminStates.waiting_for_admin_message, F.content_type.in_([
    ContentType.TEXT, ContentType.AUDIO, ContentType.VOICE, ContentType.VIDEO,
    ContentType.PHOTO, ContentType.ANIMATION, ContentType.STICKER, 
    ContentType.LOCATION, ContentType.DOCUMENT, ContentType.CONTACT,
    ContentType.VIDEO_NOTE
]))
async def handle_admin_message(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    user_link = get_user_link(user_id, first_name)  # Foydalanuvchi linki
    inline_keyboard = create_inline_keyboard(user_id)

    for admin_id in ADMINS:
        try:
            if message.text:
                await bot.send_message(
                    admin_id,
                    f"Foydalanuvchi: {user_link}\n\nXabar:\n{message.text}",
                    reply_markup=inline_keyboard,
                    parse_mode="Markdown"
                )
            elif message.photo:
                await bot.send_photo(
                    admin_id, 
                    message.photo[-1].file_id,
                    caption=f"Foydalanuvchi: {user_link}\n\nRasm xabar",
                    reply_markup=inline_keyboard,
                    parse_mode="Markdown"
                )
            elif message.voice:
                await bot.send_voice(
                    admin_id,
                    message.voice.file_id,
                    caption=f"Foydalanuvchi: {user_link}\n\nVoice xabar",
                    reply_markup=inline_keyboard,
                    parse_mode="Markdown"
                )
            # Qo'shimcha content turlari
            elif message.video:
                await bot.send_video(
                    admin_id,
                    message.video.file_id,
                    caption=f"Foydalanuvchi: {user_link}\n\nVideo xabar",
                    reply_markup=inline_keyboard,
                    parse_mode="Markdown"
                )
            # Qo'llab-quvvatlanmagan tur uchun loglash
            else:
                await bot.send_message(admin_id, f"Foydalanuvchidan yangi xabar: {user_link}")
        except Exception as e:
            logger.error(f"Xatolik adminga xabar yuborishda: {e}")

    await state.clear()
    await message.answer("Admin sizga javob berishi mumkin.", reply_markup=admin_keyboard.start_button)

# Javob callback handler
@dp.callback_query(lambda c: c.data.startswith('reply:'))
async def process_reply_callback(callback_query: CallbackQuery, state: FSMContext):
    user_id = int(callback_query.data.split(":")[1])
    await callback_query.message.answer(
        "Javobingizni yozing. Sizning javobingiz foydalanuvchiga yuboriladi.", 
        reply_markup=admin_keyboard.start_button
    )
    await state.update_data(reply_user_id=user_id)
    await state.set_state(AdminStates.waiting_for_reply_message)
    await callback_query.answer()

# Admin javobini foydalanuvchiga yuborish
@dp.message(AdminStates.waiting_for_reply_message)
async def handle_admin_reply(message: Message, state: FSMContext):
    data = await state.get_data()
    user_id = data.get('reply_user_id')

    if user_id:
        try:
            if message.text:
                await bot.send_message(user_id, f"Admin javobi:\n{message.text}")
            elif message.voice:
                await bot.send_voice(user_id, message.voice.file_id)
            elif message.photo:
                await bot.send_photo(user_id, message.photo[-1].file_id)
            elif message.video:
                await bot.send_video(user_id, message.video.file_id)
            await state.clear()
            await message.answer("Javob yuborildi!")
        except Exception as e:
            logger.error(f"Javob yuborishda xatolik: {e}")
            await message.reply("Xatolik: Javob yuborishda xato yuz berdi.")
    else:
        await message.reply("Xatolik: Javob yuborish uchun foydalanuvchi topilmadi.")
