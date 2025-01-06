from aiogram.types import Message
from loader import dp
from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.context import FSMContext
from handlers.users.nick_generator import nick_generator
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

@dp.message()
async def generate_short_nicks(message: types.Message, state: FSMContext):
    name = message.text.lower()
    await message.delete()
    await state.update_data(name=name)  
    nicknames = nick_generator(name=name)
    page_size = 10
    page_num = 0
    total_pages = (len(nicknames) + page_size - 1) // page_size
    paginated_nicknames = nicknames[page_num * page_size:(page_num + 1) * page_size]
    text = "✨ Natija : \n\n"
    for idx, nick in enumerate(paginated_nicknames, start=page_num * page_size + 1):
        text += f"{idx}. <code>{nick}</code>\n\n"

    markup = InlineKeyboardBuilder()
    if page_num > 0:
        markup.add(InlineKeyboardButton(text="⬅️", callback_data=f"short_page_{page_num-1}"))
    if page_num < total_pages - 1:
        markup.add(InlineKeyboardButton(text="➡️", callback_data=f"short_page_{page_num+1}"))
    
    await message.answer(text, reply_markup=markup.as_markup())




@dp.callback_query(lambda c: c.data.startswith("short_page_"))
async def handle_short_page(callback_query: types.CallbackQuery, state: FSMContext):
    data = callback_query.data.split("_")
    page_num = int(data[2])
    user_data = await state.get_data()
    name = user_data.get('name')
    nicknames = nick_generator(name=name)

    page_size = 10
    total_pages = (len(nicknames) + page_size - 1) // page_size
    paginated_nicknames = nicknames[page_num * page_size:(page_num + 1) * page_size]

    text = "✨ Natija : \n\n"
    for idx, nick in enumerate(paginated_nicknames, start=page_num * page_size + 1):
        text += f"{idx}. <code>{nick}</code>\n\n"

    markup = InlineKeyboardBuilder()
    if page_num > 0:
        markup.add(InlineKeyboardButton(text="⬅️", callback_data=f"short_page_{page_num-1}"))
    if page_num < total_pages - 1:
        markup.add(InlineKeyboardButton(text="➡️", callback_data=f"short_page_{page_num+1}"))

    await callback_query.message.edit_text(text, reply_markup=markup.as_markup())
    await callback_query.answer()
    