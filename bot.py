import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram import F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.client.bot import Bot, DefaultBotProperties
from aiogram.fsm.context import FSMContext
from data import config
from filterss.admin import IsBotAdminFilter
from filterss.check_sub_channel import IsCheckSubChannels
from keyboard_buttons import admin_keyboard
from states.reklama import Adverts
from paginations import pagination
from nick_generator import nick_generator
from menucommands.set_bot_commands import set_default_commands
from baza.sqlite import Database
import time

# Config fayldan ADMINS, TOKEN va CHANNELS o'zgaruvchilarini olish
ADMINS = config.ADMINS
TOKEN = config.BOT_TOKEN
CHANNELS = config.CHANNELS

# Dispatcher ob'ektini yaratish
dp = Dispatcher()

# Bot va Database ob'ektlari
bot: Bot
db: Database

# /start komandasi uchun handler
@dp.message(CommandStart())
async def start_command(message: Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name, telegram_id=telegram_id)
        await message.answer(text="Salom! Botimizga xush kelibsiz! 🎉 Siz o'ziga xos, qiziqarli va esda qolarli niklar yaratmoqchimisiz? Endi bu juda oson! 💫 Shunchaki ism kiriting va biz sizga eng zo'r variantlarni taqdim etamiz. Boshlashga tayyormisiz? 🚀")
    except:
        await message.answer(text="Salom! Botimizga xush kelibsiz! 🎉 Siz o'ziga xos, qiziqarli va esda qolarli niklar yaratmoqchimisiz? Endi bu juda oson! 💫 Shunchaki ism kiriting va biz sizga eng zo'r variantlarni taqdim etamiz. Boshlashga tayyormisiz? 🚀")

# Kanalga obuna bo'lishni tekshiruvchi handler
@dp.message(IsCheckSubChannels())
async def kanalga_obuna(message: Message):
    text = ""
    inline_channel = InlineKeyboardBuilder()
    for index, channel in enumerate(CHANNELS):
        ChatInviteLink = await bot.create_chat_invite_link(channel)
        inline_channel.add(InlineKeyboardButton(text=f"{index+1}-kanal", url=ChatInviteLink.invite_link))
    inline_channel.adjust(1, repeat=True)
    button = inline_channel.as_markup()
    await message.answer(f"{text} kanallarga azo bo'ling", reply_markup=button)

# /help komandasi uchun handler
@dp.message(Command("help"))
async def help_commands(message: Message):
    await message.answer("Yordam kerakmi? Biz sizga o'zingizga mos, noyob va original nik yaratishda yordam beramiz! 🔥 Istalgancha nik giniratsiya qiling, tanlang va boshqa hech kimga o'xshamaydigan uslubingizni yarating! 😎")

# /about komandasi uchun handler
@dp.message(Command("about"))
async def about_commands(message: Message):
    await message.answer("Nik generatsiyasi: Foydalanuvchi ism kiritganda, bot bir nechta turli xil nik variantlarini yaratadi va ularni sahifalarga bo‘lib ko‘rsatadi. Har bir sahifada 10 ta nik ko‘rsatiladi va foydalanuvchi “Orqaga” yoki “Oldinga” tugmalari yordamida sahifalarni o‘zaro o‘zgartirishi mumkin.")

# Admin bo'lishni tekshiruvchi handler
@dp.message(Command("admin"), IsBotAdminFilter(ADMINS))
async def is_admin(message: Message):
    await message.answer(text="Admin menu", reply_markup=admin_keyboard.admin_button)

# Foydalanuvchilar sonini ko'rsatuvchi handler
@dp.message(F.text == "Foydalanuvchilar soni", IsBotAdminFilter(ADMINS))
async def users_count(message: Message):
    counts = db.count_users()
    text = f"Botimizda {counts[0]} ta foydalanuvchi bor"
    await message.answer(text=text)

# Reklama yuborish komandasi uchun handler
@dp.message(F.text == "Reklama yuborish", IsBotAdminFilter(ADMINS))
async def advert_dp(message: Message, state: FSMContext):
    await state.set_state(Adverts.adverts)
    await message.answer(text="Reklama yuborishingiz mumkin !")

# Reklama xabarini foydalanuvchilarga yuboruvchi handler
@dp.message(Adverts.adverts)
async def send_advert(message: Message, state: FSMContext):
    message_id = message.message_id
    from_chat_id = message.from_user.id
    users = db.all_users_id()
    count = 0
    for user in users:
        try:
            await bot.copy_message(chat_id=user[0], from_chat_id=from_chat_id, message_id=message_id)
            count += 1
        except:
            pass
        time.sleep(0.01)
    
    await message.answer(f"Reklama {count}ta foydalanuvchiga yuborildi")
    await state.clear()


# Nik giniratsiya qiluvchi handler
@dp.message()
async def nick_generator_handler(message: Message):
    if message.content_type != 'text':
        await message.answer("Faqat matnli xabarlarni yuborishingiz mumkin.")
        await message.delete()
        return

    name = message.text.lower()
    nicknames = nick_generator(name=name)
    
    # Pagination
    page_size = 10
    page_num = 0
    total_pages = (len(nicknames) + page_size - 1) // page_size

    # Show the first page
    paginated_nicknames = nicknames[page_num * page_size:(page_num + 1) * page_size]
    text = "✨ Natija : \n\n"
    for idx, nick in enumerate(paginated_nicknames, start=page_num * page_size + 1):
        text += f"{idx}. <code>{nick}</code>\n\n"
    

    # Add pagination buttons
    markup = InlineKeyboardBuilder()
    if page_num > 0:
        markup.add(InlineKeyboardButton(text="⬅️ Orqaga", callback_data=f"page_{page_num-1}_{name}"))
    if page_num < total_pages - 1:
        markup.add(InlineKeyboardButton(text="Oldinga ➡️", callback_data=f"page_{page_num+1}_{name}"))

    await message.answer(text, reply_markup=markup.as_markup())
# Callback handler for pagination
@dp.callback_query(lambda c: c.data.startswith("page_"))
async def handle_page(callback_query: CallbackQuery):
    data = callback_query.data.split("_")
    page_num = int(data[1])
    name = data[2]  # Extract the name from the callback data
    
    # Get all nicknames again
    nicknames = nick_generator(name=name)
    
    # Pagination logic
    page_size = 10
    total_pages = (len(nicknames) + page_size - 1) // page_size
    paginated_nicknames = nicknames[page_num * page_size:(page_num + 1) * page_size]

    text = "✨ Natija : \n\n"
    for idx, nick in enumerate(paginated_nicknames, start=page_num * page_size + 1):
        text += f"{idx}. <code>{nick.upper()}</code>\n\n"
    
    # Add pagination buttons
    markup = InlineKeyboardBuilder()
    if page_num > 0:
        markup.add(InlineKeyboardButton(text="⬅️ Orqaga", callback_data=f"page_{page_num-1}_{name}"))
    if page_num < total_pages - 1:
        markup.add(InlineKeyboardButton(text="Oldinga ➡️", callback_data=f"page_{page_num+1}_{name}"))
    
    await callback_query.message.edit_text(text, reply_markup=markup.as_markup())
    await callback_query.answer()


# Bot ishga tushganligini adminlarga xabar beruvchi funksiya
@dp.startup()
async def on_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin), text="Bot ishga tushdi")
        except Exception as err:
            logging.exception(err)

# Bot to'xtaganda adminlarga xabar beruvchi funksiya
@dp.shutdown()
async def off_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin), text="Bot ishdan to'xtadi!")
        except Exception as err:
            logging.exception(err)

# O'rta dasturlarni sozlash uchun funksiya
def setup_middlewares(dispatcher: Dispatcher, bot: Bot) -> None:
    """MIDDLEWARE"""
    from middlewares.throttling import ThrottlingMiddleware

    dispatcher.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))

# Asosiy funksiya
async def main() -> None:
    global bot, db
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    db = Database(path_to_db="main.db")
    await set_default_commands(bot)
    setup_middlewares(dispatcher=dp, bot=bot)
    await dp.start_polling(bot)

# Agar skript to'g'ridan-to'g'ri ishga tushirilsa
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
