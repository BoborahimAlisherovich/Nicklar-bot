
from aiogram.types import Message
from loader import dp, db
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
import json

def load_texts():
    with open("languages.json", "r", encoding="utf-8") as f:
        return json.load(f)

texts = load_texts()

def is_guied_us_message(message_text):
    possible_texts = [
        texts.get(lang, {}).get("menu", {}).get("menu_button_4", "")
        for lang in texts
    ]
    return message_text in possible_texts
# ["📙Qo'llanma","📙 Guide","📙 Гид"]
@dp.message(lambda message: is_guied_us_message(message.text))
async def guied_us(message: Message, state: FSMContext):
    telegram_id = message.from_user.id

    user = db.select_user_by_id(telegram_id=telegram_id)

    language = "uz" 

    if user:
        language = user[2]
    text = texts.get(language, {}).get("guide", "Tilga mos matn topilmadi.")

    await message.answer(text, parse_mode='html')
    await state.clear()

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)






NAMES_PER_PAGE = 1 
NAMES_PER_PAGES = 10 
def get_pagination_keyboard(current_page):
    buttons = []
    if current_page > 0:
        buttons.append(InlineKeyboardButton(text="⬅️", callback_data=f"prev:{current_page - 1}"))
    if (current_page + 1) * NAMES_PER_PAGE < len(allah_names):
        buttons.append(InlineKeyboardButton(text="➡️", callback_data=f"next:{current_page + 1}"))
    return InlineKeyboardMarkup(inline_keyboard=[buttons])

# Trenddagi Stikerlar sahifa matni
def get_names_page(page):
    start = page * NAMES_PER_PAGE
    end = start + NAMES_PER_PAGE
    return "\n\n".join(map(str, allah_names[start:end]))

def get_pagination_keyboardd(current_pages):
    buttons = []
    if current_pages > 0:
        buttons.append(InlineKeyboardButton(text="⬅️", callback_data=f"prev1:{current_pages - 1}"))
    if (current_pages + 1) * NAMES_PER_PAGES < len(top_nick):
        buttons.append(InlineKeyboardButton(text="➡️", callback_data=f"next1:{current_pages + 1}"))
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


@dp.message(lambda message: message.text in ["🔥Mashhur Stikerlar", "🔥 Popular Stickers", "🔥 Популярные стикеры"])
async def send_names(message: types.Message, state: FSMContext):
    current_page = 0
    await message.answer(
        text="```" + get_names_page(current_page) + "```",
        reply_markup=get_pagination_keyboard(current_page),
        parse_mode="Markdown"
    )
    await state.clear()

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

@dp.message(lambda message: message.text in ["✨ Top nik","✨ Top Nick","✨ Топ ник"])
async def send_namess(message: types.Message, state: FSMContext):
    current_page = 0
    await message.answer(
        text=get_names_pages(current_page),
        reply_markup=get_pagination_keyboardd(current_page),
        parse_mode="HTML"
    )
    await state.clear()

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