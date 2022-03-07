from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



def rasmni_korish(jami, call_1, call_2, check):
	# print(call_1)
	birinchi_rasmni_korish = InlineKeyboardMarkup(
		inline_keyboard=[
		[
			InlineKeyboardButton(text="⬅️", callback_data=f"{call_1}"),
			InlineKeyboardButton(text=f"1 / {jami}", callback_data="place"),
			InlineKeyboardButton(text="➡️", callback_data=f"{call_2}"),
		],
		[
			InlineKeyboardButton(text="✅ Tanlash", callback_data=f"{check}"),
		],
	])
	return birinchi_rasmni_korish



def change_photo(tr,jami, call_1, call_2, check):
	# print(call_2)

	change_photo_btn = InlineKeyboardMarkup(
		inline_keyboard=[
		[
		InlineKeyboardButton(text="⬅️", callback_data=f"{call_1}"),
		InlineKeyboardButton(text=f"{tr} / {jami}", callback_data="place"),
		InlineKeyboardButton(text="➡️", callback_data=f"{call_2}"),
	],
		[
			InlineKeyboardButton(text="✅ Tanlash", callback_data=f"{check}"),
		],
	])

	return change_photo_btn