
from aiogram.types import Message
from loader import dp
from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboard_buttons import admin_keyboard
import logging
from aiogram import F
from handlers.users.emojelar import allah_names, top_nick
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types


    




#Qo'llanma
@dp.message(F.text == "📙Qo'llanma")
async def guide_handler(message: Message, state: FSMContext):
    text = """
  Botdan foydalanish uchun yo'riqnoma:
💡 Botdan unumli foydalaning va o'z uslubingizni yarating!

1️⃣ Qisqa nik yaratish: Botdan qisqa va chiroyli niklar olish uchun ismingizni kiriting – bot sizga noyob variantlarni taklif qiladi.
2️⃣ Qo'llanma bilan tanishing: Botdan to'g'ri foydalanishni o'rganish uchun '📙 Qo'llanma' tugmasini bosing va barcha funksiyalar haqida batafsil ma'lumot oling.
3️⃣ Top niklar to'plami: Eng chiroyli va mashhur niklar ro'yxatini ko'ring, o'ziga xos uslubingizni toping!\nEslatib o‘tamiz 1- raqamdagi ko‘rinmas nick
4️⃣ Trenddagi stiklarlar: Siz uchun eng chiroyli va dolzarb stiklarlar to'plami tayyor! Ularni sinab ko'ring va muloqotingizni yanada qiziqarli qiling.
5️⃣ Admin bilan bog'laning: Savollaringiz yoki takliflaringiz bo'lsa, '👨‍💼 Admin' tugmasini bosing va o'z xabaringizni yuboring.

✨ Botdan foydalanib, o'z uslubingizni yarating va ijodingizni bahramand qiling!  """
    await message.answer(text=text)
    await state.clear()

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)






NAMES_PER_PAGE = 1  # Trenddagi Stikerlar uchun sahifadagi elementlar soni
NAMES_PER_PAGES = 10  # Top Nick uchun sahifadagi elementlar soni

# Trenddagi Stikerlar pagination uchun klaviatura
def get_pagination_keyboard(current_page):
    buttons = []
    if current_page > 0:
        buttons.append(InlineKeyboardButton(text="⬅️ Orqaga", callback_data=f"prev:{current_page - 1}"))
    if (current_page + 1) * NAMES_PER_PAGE < len(allah_names):
        buttons.append(InlineKeyboardButton(text="Oldinga ➡️", callback_data=f"next:{current_page + 1}"))
    return InlineKeyboardMarkup(inline_keyboard=[buttons])

# Trenddagi Stikerlar sahifa matni
def get_names_page(page):
    start = page * NAMES_PER_PAGE
    end = start + NAMES_PER_PAGE
    return "\n\n".join(map(str, allah_names[start:end]))

# Top Nick pagination uchun klaviatura
def get_pagination_keyboardd(current_pages):
    buttons = []
    if current_pages > 0:
        buttons.append(InlineKeyboardButton(text="⬅️ Orqaga", callback_data=f"prev1:{current_pages - 1}"))
    if (current_pages + 1) * NAMES_PER_PAGES < len(top_nick):
        buttons.append(InlineKeyboardButton(text="Oldinga ➡️", callback_data=f"next1:{current_pages + 1}"))
    return InlineKeyboardMarkup(inline_keyboard=[buttons])
def get_names_pages(page):
    start = page * NAMES_PER_PAGES
    end = start + NAMES_PER_PAGES
    paginated_nicknamess = top_nick[start:end]
    korinmas = "Ko'rinmas Nick"
    return "\n\n\n".join([
        f"{idx + start + 1}- <code>{'⠿' if nicks.strip() == 'ㅤㅤㅤ ' else nicks}</code> <i>{korinmas if idx + start == 0 else ''}</i>"
        for idx, nicks in enumerate(paginated_nicknamess)
    ])
# Trenddagi Stikerlar uchun handler
@dp.message(F.text == "🔥Trenddagi Stikerlar")
async def send_names(message: types.Message, state: FSMContext):
    current_page = 0
    await message.answer(
        text="```" + get_names_page(current_page) + "```",
        reply_markup=get_pagination_keyboard(current_page),
        parse_mode="Markdown"
    )
    await state.clear()

# Trenddagi Stikerlar pagination callback handler
@dp.callback_query(lambda c: c.data and (c.data.startswith('next:') or c.data.startswith('prev:')))
async def process_pagination(callback_query: types.CallbackQuery, state: FSMContext):
    action, page = callback_query.data.split(':')
    current_page = int(page)
    await callback_query.message.edit_text(
        text="```" + get_names_page(current_page) + "```",
        reply_markup=get_pagination_keyboard(current_page),
        parse_mode="Markdown"
    )
    await callback_query.answer()
    await state.clear()

# Top Nick uchun handler
@dp.message(F.text == "✨Top nick")
async def send_namess(message: types.Message, state: FSMContext):
    current_page = 0
    await message.answer(
        text=get_names_pages(current_page),
        reply_markup=get_pagination_keyboardd(current_page),
        parse_mode="HTML"
    )
    await state.clear()

# Top Nick pagination callback handler
@dp.callback_query(lambda c: c.data and (c.data.startswith('next1:') or c.data.startswith('prev1:')))
async def process_paginations(callback_query: types.CallbackQuery, state: FSMContext):
    action, page = callback_query.data.split(':')
    current_page = int(page)
    await callback_query.message.edit_text(
        text=get_names_pages(current_page),
        reply_markup=get_pagination_keyboardd(current_page),
        parse_mode="HTML"
    )
    await callback_query.answer()
    await state.clear()