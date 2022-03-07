from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



bayramlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👩🏼 8-Mart 🌹"),           
            # KeyboardButton(text="Tugi'lgan kun 📅"),           
             
        ],
        # [
        #     KeyboardButton(text="Navro'z"), 
        # ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Qaysi bayram uchun tabriknoma kerak?"

)


def create_btn(malum, nomalum):
	qanday_btn = ReplyKeyboardMarkup(
	    keyboard=[
	        [
	            KeyboardButton(text=f"{malum}"),           
	            KeyboardButton(text=f"{nomalum}"),           
	             
	        ],
	        [
	            KeyboardButton(text="🔙 Ortga"), 
	        ],
	    ],
	    resize_keyboard=True,
	    one_time_keyboard=True,	    
	    input_field_placeholder="Qanday usuldagi tabriknoma kerak?"

	)
	return qanday_btn