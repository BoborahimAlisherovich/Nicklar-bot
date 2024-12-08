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
            KeyboardButton(text="📙Qo'llanma"),
             KeyboardButton(text="Top nick"),
 
        ],
            [
         
            KeyboardButton(text="Trenddagi Stikerlar"),
             KeyboardButton(text="👨‍💼Admin"),
        ],
       
        
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