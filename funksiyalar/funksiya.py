from aiogram.utils.keyboard import InlineKeyboardBuilder


# Function to create inline keyboard for reply
def create_inline_keyboard(user_id):
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text="Javob berish",
        callback_data=f"reply:{user_id}"
    )

    return keyboard_builder.as_markup()