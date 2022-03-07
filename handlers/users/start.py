from aiogram import types
from pprint import pprint as print
from filters import IsPrivate


from aiogram.dispatcher.filters.builtin import CommandStart

import asyncio
import sqlite3
from keyboards.default.def_btn import bayramlar


from data.config import ADMINS, GROUP_CHAT_ID
from loader import dp, db, bot

################### user_id=ADMINS ni ochirish kerek ################3333

@dp.message_handler(IsPrivate(),CommandStart())
async def bot_start(message: types.Message):
	name = message.from_user.full_name
	try:
		db.add_user(id=message.from_user.id,  name=name)
		await bot.send_message(GROUP_CHAT_ID, f"{name} start bosdi.\nid:<a href='tg://user?id={message.from_user.id}'> {message.from_user.id} </a>")
	except sqlite3.IntegrityError as err:
		pass
	await message.answer(f"Salom, {message.from_user.full_name}! Bu bot orqali siz o'z yaqinlaringiz uchun rasmli, matnli tabriknomalar yasashingiz mumkin.", reply_markup=bayramlar)
	await message.answer("Qanday bayram uchun tabriknomalar tayyorlamoqchisiz?")
	# print(message)
	# await bot.forward_message(message.from_user.id,  message.from_user.id, message.message_id)
