import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram import F
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.client.bot import Bot, DefaultBotProperties
from aiogram.fsm.context import FSMContext
from data import config
from filterss.admin import IsBotAdminFilter
from filterss.check_sub_channel import IsCheckSubChannels
from keyboard_buttons import admin_keyboard
from states.reklama import Adverts
from menucommands.set_bot_commands import set_default_commands
from baza.sqlite import Database
from nick_generator import nick_generator
import time
from states.bulimlar import AdminStates,ShortNickStates,LongNickStates
from aiogram import types
import logging
from funksiyalar.funksiya import create_inline_keyboard
from aiogram.types import CallbackQuery, ContentType
from aiogram.fsm.context import FSMContext

ADMINS = config.ADMINS
TOKEN = config.BOT_TOKEN
CHANNELS = config.CHANNELS

dp = Dispatcher()

bot: Bot
db: Database

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


@dp.message(Command("help"))
async def help_commands(message: Message,state:FSMContext):
    await message.answer("Yordam kerakmi? Biz sizga o'zingizga mos, noyob va original nik yaratishda yordam beramiz! 🔥 Istalgancha nik giniratsiya qiling, tanlang va boshqa hech kimga o'xshamaydigan uslubingizni yarating! 😎",reply_markup=admin_keyboard.start_button)
    await state.clear()
  


@dp.message(Command("about"))
async def about_commands(message: Message,state:FSMContext):
    await message.answer("Nik generatsiyasi: Foydalanuvchi ism kiritganda, bot bir nechta turli xil nik variantlarini yaratadi va ularni sahifalarga bo‘lib ko‘rsatadi. Har bir sahifada 10 ta nik ko‘rsatiladi va foydalanuvchi “Orqaga” yoki “Oldinga” tugmalari yordamida sahifalarni o‘zaro o‘zgartirishi mumkin.",reply_markup=admin_keyboard.start_button)
    await state.clear()

@dp.message(Command("admin"), IsBotAdminFilter(ADMINS))
async def is_admin(message: Message):
    await message.answer(text="Admin menu", reply_markup=admin_keyboard.admin_button)


@dp.message(F.text == "Foydalanuvchilar soni", IsBotAdminFilter(ADMINS))
async def users_count(message: Message):
    counts = db.count_users()
    text = f"Botimizda {counts[0]} ta foydalanuvchi bor"
    await message.answer(text=text)


@dp.message(F.text == "Reklama yuborish", IsBotAdminFilter(ADMINS))
async def advert_dp(message: Message, state: FSMContext):
    await state.set_state(Adverts.adverts)
    await message.answer(text="Reklama yuborishingiz mumkin !")


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




@dp.message(F.text == "♻️ Orqaga")
async def orqaga(message:Message,state:FSMContext):
    await  state.clear()
    await message.answer("Ism kiriting",reply_markup=admin_keyboard.start_button)
    




#Qo'llanma
@dp.message(F.text == "📙Qo'llanma")
async def guide_handler(message: Message, state: FSMContext):
    text = """
  Botdan foydalanish uchun yo'riqnoma:
💡 Botdan unumli foydalaning va o'z uslubingizni yarating!

1️⃣ Qisqa nik yaratish: Botdan qisqa va chiroyli niklar olish uchun ismingizni kiriting – bot sizga noyob variantlarni taklif qiladi.
2️⃣ Qo'llanma bilan tanishing: Botdan to'g'ri foydalanishni o'rganish uchun '📙 Qo'llanma' tugmasini bosing va barcha funksiyalar haqida batafsil ma'lumot oling.
3️⃣ Top niklar to'plami: Eng chiroyli va mashhur niklar ro'yxatini ko'ring, o'ziga xos uslubingizni toping!
4️⃣ Trenddagi stiklarlar: Siz uchun eng chiroyli va dolzarb stiklarlar to'plami tayyor! Ularni sinab ko'ring va muloqotingizni yanada qiziqarli qiling.
5️⃣ Admin bilan bog'laning: Savollaringiz yoki takliflaringiz bo'lsa, '👨‍💼 Admin' tugmasini bosing va o'z xabaringizni yuboring.

✨ Botdan foydalanib, o'z uslubingizni yarating va ijodingizni bahramand qiling!  """
    await message.answer(text=text)

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



from emojelar import allah_names, top_nick
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
# from aiogram.dispatcher.filters import Text
# from aiogram.dispatcher import FSMContext

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
    
    return "\n\n".join([f"{idx + start + 1}- <code>{nicks}</code>" for idx, nicks in enumerate(paginated_nicknamess)])

# Trenddagi Stikerlar uchun handler
@dp.message(F.text == "Trenddagi Stikerlar")
async def send_names(message: types.Message, state: FSMContext):
    await message.delete()
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
@dp.message(F.text == "Top nick")
async def send_namess(message: types.Message, state: FSMContext):
    await message.delete()
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

@dp.message(F.text == "👨‍💼Admin")
async def admin_message(message: Message, state: FSMContext):
    await message.answer("Admin uchun xabar yuboring:",reply_markup=admin_keyboard.orqaga_button)
    await state.set_state(AdminStates.waiting_for_admin_message)

@dp.message(AdminStates.waiting_for_admin_message, F.content_type.in_([
    ContentType.TEXT, ContentType.AUDIO, ContentType.VOICE, ContentType.VIDEO,
    ContentType.PHOTO, ContentType.ANIMATION, ContentType.STICKER, 
    ContentType.LOCATION, ContentType.DOCUMENT, ContentType.CONTACT,
    ContentType.VIDEO_NOTE
]))

async def handle_admin_message(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name or ""  # Some users may not have a last name


    if username:
      user_identifier = f"@{username}"
    else:
        user_link = f"[{first_name} {last_name}](tg://user?id={user_id})"
        user_identifier = user_link


    video_note = message.video_note
    inline_keyboard = create_inline_keyboard(user_id)
    for admin_id in ADMINS:
        try:
            if video_note:
                # print('adfs', message.video_note.file_id)
                await bot.send_video_note(
                    admin_id,
                    video_note.file_id,
                    reply_markup=inline_keyboard,
                     parse_mode="MarkdownV2" 
                )
            elif message.text:
                await bot.send_message(
                    admin_id,
                    f"Foydalanuvchi: {user_identifier}\nXabar:\n{message.text}",
                    reply_markup=inline_keyboard,
                     parse_mode="MarkdownV2" 
                )
            elif message.audio:
                await bot.send_audio(
                    admin_id,
                    message.audio.file_id,
                    caption=f"Foydalanuvchi: {user_identifier}\nAudio xabar",
                    reply_markup=inline_keyboard,
                     parse_mode="MarkdownV2" 
                )
            elif message.voice:
                await bot.send_voice(
                    admin_id,
                    message.voice.file_id,
                    caption=f"Foydalanuvchi: {user_identifier}\nVoice xabar",
                    reply_markup=inline_keyboard,
                     parse_mode="MarkdownV2" 
                )
            elif message.video:
                await bot.send_video(
                    admin_id,
                    message.video.file_id,
                    caption=f"Foydalanuvchi: {user_identifier}\nVideo xabar",
                    reply_markup=inline_keyboard,
                     parse_mode="MarkdownV2" 
                )
            elif message.photo:
                await bot.send_photo(
                    admin_id,
                    message.photo[-1].file_id,  # using the highest resolution photo
                    caption=f"Foydalanuvchi: {user_identifier}\nRasm xabar",
                    reply_markup=inline_keyboard,
                     parse_mode="MarkdownV2" 
                )
            elif message.animation:
                await bot.send_animation(
                    admin_id,
                    message.animation.file_id,
                    caption=f"Foydalanuvchi: {user_identifier}\nGIF xabar",
                    reply_markup=inline_keyboard,
                     parse_mode="MarkdownV2" 
                )
            elif message.sticker:
                await bot.send_sticker(
                    admin_id,
                    message.sticker.file_id,
                    reply_markup=inline_keyboard,
                     parse_mode="MarkdownV2" 
                )
            elif message.location:
                await bot.send_location(
                    admin_id,
                    latitude=message.location.latitude,
                    longitude=message.location.longitude,
                    reply_markup=inline_keyboard,
                     parse_mode="MarkdownV2" 
                )
            elif message.document:
                await bot.send_document(
                    admin_id,
                    message.document.file_id,
                    caption=f"Foydalanuvchi: {user_identifier}\nHujjat xabar",
                    reply_markup=inline_keyboard,
                     parse_mode="MarkdownV2" 
                )
            elif message.contact:
                await bot.send_contact(
                    admin_id,
                    phone_number=message.contact.phone_number,
                    first_name=message.contact.first_name,
                    last_name=message.contact.last_name or "",
                    reply_markup=inline_keyboard,
                     parse_mode="MarkdownV2" 
                )
        except Exception as e:
            logging.error(f"Error sending message to admin {admin_id}: {e}")

    await state.clear()
    await bot.send_message(user_id, "Admin sizga javob berishi mumkin.", reply_markup=admin_keyboard.start_button)


@dp.callback_query(lambda c: c.data.startswith('reply:'))
async def process_reply_callback(callback_query: CallbackQuery, state: FSMContext):
    user_id = int(callback_query.data.split(":")[1])
    await callback_query.message.answer("Javobingizni yozing. Sizning javobingiz foydalanuvchiga yuboriladi.",reply_markup=admin_keyboard.start_button)
    await state.update_data(reply_user_id=user_id)
    await state.set_state(AdminStates.waiting_for_reply_message)
    await callback_query.answer()


@dp.message(AdminStates.waiting_for_reply_message)
async def handle_admin_reply(message: Message, state: FSMContext):
    data = await state.get_data()
    original_user_id = data.get('reply_user_id')

    if original_user_id:
        try:
            if message.text:
                await bot.send_message(original_user_id, f"Admin javobi:\n{message.text}", reply_markup=admin_keyboard.start_button)
            
            elif message.voice:
                await bot.send_voice(original_user_id, message.voice.file_id, reply_markup=admin_keyboard.start_button)

            elif message.video_note:
                await bot.send_video_note(original_user_id, message.video_note.file_id, reply_markup=admin_keyboard.start_button)

            elif message.audio:
                await bot.send_audio(original_user_id, message.audio.file_id, reply_markup=admin_keyboard.start_button)
            
            elif message.sticker:
                await bot.send_sticker(original_user_id, message.sticker.file_id, reply_markup=admin_keyboard.start_button)
            
            elif message.video:
                await bot.send_video(original_user_id, message.video.file_id, reply_markup=admin_keyboard.start_button)

            await state.clear()  # Clear state after sending the reply
        except Exception as e:
            logger.error(f"Error sending reply to user {original_user_id}: {e}")
            await message.reply("Xatolik: Javob yuborishda xato yuz berdi.")
    else:
        await message.reply("Xatolik: Javob yuborish uchun foydalanuvchi ID topilmadi.")



# nick funksiya 
@dp.message()
async def generate_short_nicks(message: types.Message, state: FSMContext):
    name = message.text.lower()
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
        markup.add(InlineKeyboardButton(text="⬅️ Orqaga", callback_data=f"short_page_{page_num-1}"))
    if page_num < total_pages - 1:
        markup.add(InlineKeyboardButton(text="Oldinga ➡️", callback_data=f"short_page_{page_num+1}"))

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
        markup.add(InlineKeyboardButton(text="⬅️ Orqaga", callback_data=f"short_page_{page_num-1}"))
    if page_num < total_pages - 1:
        markup.add(InlineKeyboardButton(text="Oldinga ➡️", callback_data=f"short_page_{page_num+1}"))

    await callback_query.message.edit_text(text, reply_markup=markup.as_markup())
    await callback_query.answer()
    


@dp.startup()
async def on_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin), text="Bot ishga tushdi")
        except Exception as err:
            logging.exception(err)


@dp.shutdown()
async def off_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin), text="Bot ishdan to'xtadi!")
        except Exception as err:
            logging.exception(err)


def setup_middlewares(dispatcher: Dispatcher, bot: Bot) -> None:
    """MIDDLEWARE"""
    from middlewares.throttling import ThrottlingMiddleware

    dispatcher.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))


async def main() -> None:
    global bot, db
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    db = Database(path_to_db="main.db")
    await set_default_commands(bot)
    setup_middlewares(dispatcher=dp, bot=bot)
    await dp.start_polling(bot)

    await bot.delete_webhook(drop_pending_updates=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    

