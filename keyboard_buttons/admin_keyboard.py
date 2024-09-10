from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Foydalanuvchilar soni"),
            KeyboardButton(text="Reklama yuborish"),
        ]
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)


start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✍️ Qisqa nick"),
    
        ],
         [
            KeyboardButton(text="📙Qo'llanma"),
 
        ],
          [
         
            KeyboardButton(text="👨‍💼Admin"),
        ]
        
        
    ],
  resize_keyboard=True
)


orqaga_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="♻️ Orqaga"),        
        ]      
    ],
  resize_keyboard=True
)