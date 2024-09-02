from aiogram.fsm.state import State, StatesGroup

# Define admin states
class AdminStates(StatesGroup):
    waiting_for_admin_message = State()
    waiting_for_reply_message = State()


class ShortNickStates(StatesGroup):
    waiting_for_name = State()

class LongNickStates(StatesGroup):
    waiting_for_text = State()
    waiting_for_number = State()