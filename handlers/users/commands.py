import asyncio
from aiogram.types import Message, CallbackQuery, InputMedia, ReplyKeyboardRemove

from aiogram import types

from data.config import ADMINS, GROUP_CHAT_ID
from loader import dp, db, bot

from keyboards.default.def_btn import bayramlar, create_btn
from keyboards.inline.inline_btn import rasmni_korish, change_photo

# from telegram import InputMediaPhoto
from aiogram.dispatcher import FSMContext


from PIL import Image, ImageFont, ImageDraw
import os
from data.sher import sherlar
from random import randint
from datetime import datetime, timedelta

# from handlers.users.photo_redaktor import rasm_qayta_ishla



def rasm_qayta_ishla(user_id, ism):
	fonts = '01ANTQUABI','02ANTQUABI','03Gstswzrm', '04BRITANIC', '05Gstswzrm', '06Gstswzrm', '07BRITANIC', '08Gstswzrm', '09TR Kastler Bold Italik', '10TR Renfrew', '11HARLOWSI','12HARLOWSI','13HARLOWSI'
	shrift = [92, 102, 225, 105, 80, 40, 95, 50, 100, 40, 45, 105, 105]
	coor = [(500,310), (570,100), (2600,1890), (700,80), (380,110), (230,55), (70,75), (180,185), (175,145), (55,65), (40,45), (120,75), (230,345)]
	color = [(255,40,0), (25,0,30), (55,190,30), (55,190,30), (55,190,30), (25,220,150), (255,10,10), (155,0,0), (255,20,150), (255,100,0), (0,255,0), (0,255,0), (90,50,0)]
	tr = 0
	i = 0
	
# img = Image.open(f"media/photo/8-mart/nomli_{tr}.jpg")

# if tr == 1:
	for font in fonts:
		# print(type(font[i]))
		# global tr
		tr += 1
		img = Image.open(f"media/photo/8-mart/nomli_{tr}.jpg")

		font = ImageFont.truetype(f"media/fonts/{font[2:]}.ttf", shrift[i])  ## impact, arial
	# font = ImageFont.truetype("resources/HelveticaNeueLight.ttf", fontsize)
		draw = ImageDraw.Draw(img)

		draw.text(coor[i], ism, color[i], font=font)
		# draw.text((640,475), iftor, (0,190,120), font=font2)

		img.save(f"media/photo_redaktor_1/{user_id}_{tr}.jpg")

		i += 1

        # users = db.select_all_users()
        # for user in users:
        #     vaqti_tugash = (datetime.now()+timedelta(minutes=1)).strftime("%X")
        #     date_update = user[2]
        #     if date_update:
        #         if str(date_update) > vaqti_tugash:
        #         print(vaqti_tugash)


@dp.message_handler(text="🔙 Ortga")
async def get_all_users(message: types.Message):
	await message.answer("Bayramlardan birini tanlang", reply_markup=bayramlar)

	try:
		rek = f"\n🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n🌺 8- mart 'Xalqaro xotin-qizlar kuni' bayrmi bilan tabriklayman! 🌷 Doimo yuzingizdan kulgu, labingizdan tabassum, ko'zlaringizdan esa baxt uchqunlari arimasin. 💐"
		rek += "🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n\n@tabriknoma_yasovchi_bot"
		caption_ = caption + rek
		new_photo = open(f'media/photo_redaktor_1/{message.from_user.id}_{tr_1}.jpg', 'rb')
		bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption_), chat_id=message.chat.id, message_id=rasmni_korsatish.message_id)	
		
		try:
			idl = message.from_user.id
			for i in range(1,14):
				path = str(idl)+"_"+str(i)+".jpg"
				os.unlink(f"media/photo_redaktor_1/{path}")
			
		except Exception as e:
			# print(e)
			pass
	except Exception as e:
		pass

		
	try:
		
	# call.answer(f"{tr_1} - rasm")
		rek = "\n🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n🌺 8- mart 'Xalqaro xotin-qizlar kuni' bayrmi bilan tabriklayman! 🌷 Doimo yuzingizdan kulgu arimasin. 💐"
		rek += "🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n\n@tabriknoma_yasovchi_bot"
		caption_ = caption + rek


		new_photo = open(f'media/photo/8-mart/nomsiz_{tr_1}.jpg', 'rb')
		bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption_), chat_id=message.chat.id, message_id=nomsiz_rasm.message_id)	

	except Exception as e:
		pass

	# os.remove(f'media/photo/8-mart/{call.from_user.id}_{tr_1}.jpg')
	




################### user_id=ADMINS ni ochirish kerek ################3333
@dp.message_handler(text="👩🏼 8-Mart 🌹")
async def get_all_users(message: types.Message):


    await message.answer(f"Qanday usulda 8- mart uchun tabriknoma yasamoqchisiz? ", reply_markup=create_btn("👩 Ism yoziladigan", "👤 Ism yozilmaydigan"))



##### barcha nomsiz rasmlar
jami_nomsiz = 20

##### barcha nomli rasmlar
jami_nomli = 13

tr_1 = 1
ism = ""


@dp.message_handler(text="👤 Ism yozilmaydigan")
async def get_all_users(message: types.Message):
	# global call_1
	# call_1 = "ortga_8-mart_2"
	# global call_2
	# call_2 = "oldinga_8-mart_2"
	global check
	check = "8-mart-ismsiz"
	global tr_1
	tr_1 = 1
	# print("1")
	global nomsiz_rasm

	global caption
	caption = sherlar[f"{randint(1, 10)}"]
	try:
		
	# await call.answer(f"{tr_1} - rasm")
		rek = "\n🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n🌺 8- mart 'Xalqaro xotin-qizlar kuni' bayrmi bilan tabriklayman! 🌷 Doimo yuzingizdan kulgu arimasin. 💐"
		rek += "🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n\n@tabriknoma_yasovchi_bot"
		caption_ = caption + rek


		new_photo = open(f'media/photo/8-mart/nomsiz_{tr_1}.jpg', 'rb')
		await bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption_), chat_id=message.chat.id, message_id=nomsiz_rasm.message_id)	

	except Exception as e:
		pass

	try:
		rek = f"\n🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n🌺 8- mart 'Xalqaro xotin-qizlar kuni' bayrmi bilan tabriklayman! 🌷  Doimo yuzingizdan kulgu, labingizdan tabassum, ko'zlaringizdan esa baxt uchqunlari arimasin. 💐"
		rek += "🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n\n@tabriknoma_yasovchi_bot"
		caption_ = caption + rek

		new_photo = open(f'media/photo_redaktor_1/{message.from_user.id}_{tr_1}.jpg', 'rb')
		await bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption_), chat_id=message.chat.id, message_id=rasmni_korsatish.message_id)	
		
		try:
			idl = message.from_user.id
			for i in range(1,14):
				path = str(idl)+"_"+str(i)+".jpg"
				os.unlink(f"media/photo_redaktor_1/{path}")
			
		except Exception as e:
			# print(e)
			pass
	except Exception as e:
		pass
	nomsiz_rasm = await message.answer_photo(photo=open("media/photo/8-mart/nomsiz_1.jpg","rb"),caption=caption, reply_markup=rasmni_korish(jami_nomsiz, "ortga_8-mart_2", "oldinga_8-mart_2", check))




@dp.callback_query_handler(text="oldinga_8-mart_2")
async def change_(call: CallbackQuery):
	# await call.message.delete()
	# print("2")

	global tr_1
	tr_1 += 1

	if tr_1>jami_nomsiz:
		tr_1 -= 1
		await call.answer("Bu oxirgi rasm")
	else:
		# await call.message.answer_photo(photo=open(f"media/photo/8-mart{tr_1}.jpg","rb"), caption=f"O'zingizga yoqqan rasmni tanlang", reply_markup=change_photo(tr_1))


		global caption
		caption = sherlar[f"{randint(1, 10)}"]
		
		new_photo = open(f'media/photo/8-mart/nomsiz_{tr_1}.jpg', 'rb')
		await bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption), chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=change_photo(tr_1, jami_nomsiz, "ortga_8-mart_2", "oldinga_8-mart_2", check))	

		# await call.message.edit_media(media=open('media/photo/8-mart3.jpg', 'rb') )




@dp.callback_query_handler(text="ortga_8-mart_2")
async def change_(call: CallbackQuery):
	# await call.message.delete()
	global tr_1
	tr_1 -= 1

	if tr_1==0:
		tr_1 += 1
		await call.answer("Bu birinchi rasm")
	else:
		# await call.message.answer_photo(photo=open(f"media/photo/8-mart{tr_1}.jpg","rb"), caption=f"O'zingizga yoqqan rasmni tanlang", reply_markup=change_photo(tr_1))

		global caption
		caption = sherlar[f"{randint(1, 10)}"]
		

		new_photo = open(f'media/photo/8-mart/nomsiz_{tr_1}.jpg', 'rb')
		await bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption), chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=change_photo(tr_1, jami_nomsiz, "ortga_8-mart_2", "oldinga_8-mart_2", check))	

		# await call.message.edit_media(media=open('media/photo/8-mart3.jpg', 'rb') )















###################   8- mart uchun ism yoziladigan  bolim ###############333

@dp.message_handler(text="👩 Ism yoziladigan", state=None)
async def get_all_users(message: types.Message, state=FSMContext):

	global tr_1
	tr_1 = 1
	try:
		rek = f"\n🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n🌺 8- mart 'Xalqaro xotin-qizlar kuni' bayrmi bilan tabriklayman! 🌷 Doimo yuzingizdan kulgu, labingizdan tabassum, ko'zlaringizdan esa baxt uchqunlari arimasin. 💐"
		rek += "🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n\n@tabriknoma_yasovchi_bot"
		caption_ = caption + rek
		new_photo = open(f'media/photo_redaktor_1/{message.from_user.id}_{tr_1}.jpg', 'rb')
		await bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption_), chat_id=message.chat.id, message_id=rasmni_korsatish.message_id)	
		

		########### eski rasmlarini ochiradi #############
		try:
			idl = message.from_user.id
			for i in range(1,14):
				path = str(idl)+"_"+str(i)+".jpg"
				os.unlink(f"media/photo_redaktor_1/{path}")
			
		except Exception as e:
			# print(e)
			pass

	except Exception as e:
		pass

	try:
		
	# await call.answer(f"{tr_1} - rasm")
		rek = "\n🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n🌺 8- mart 'Xalqaro xotin-qizlar kuni' bayrmi bilan tabriklayman! 🌷 Doimo yuzingizdan kulgu arimasin. 💐"
		rek += "🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n\n@tabriknoma_yasovchi_bot"
		caption_ = caption + rek


		new_photo = open(f'media/photo/8-mart/nomsiz_{tr_1}.jpg', 'rb')
		await bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption_), chat_id=message.chat.id, message_id=nomsiz_rasm.message_id)	

	except Exception as e:
		pass


	vaqti = datetime.now().strftime("%X")
	db.update_user_email(email=vaqti, id=message.from_user.id)
    # user = db.select_user(id=message.from_user.id)
    # await message.answer(f"Baza yangilandi: {user}")

	await message.answer("Kim uchun tabriknoma yasatmoqchisiz? \n\nIsmini kiriting:", reply_markup=ReplyKeyboardRemove()) 
	await state.set_state("8-mart-ism")


@dp.message_handler(state="8-mart-ism")
async def get_all_users(message: types.Message, state=FSMContext):
	await state.finish()


	global call_1
	call_1 = "ortga_8-mart_1"
	global call_2
	call_2 = "oldinga_8-mart_1"
	global check
	check = "8-mart-ismli"
	global ism
	ism = message.text
	# await message.answer("Kim uchun tabriknoma yasatmoqchisiz? \nIsmini kiriitng:") 
	# print(ism)
	await message.answer("O'zingizga yoqqan tabriknomani tanlang.", reply_markup=create_btn("👩 Ism yoziladigan", "👤 Ism yozilmaydigan"))
	rasm_qayta_ishla(message.from_user.id, ism)

	global caption
	caption = sherlar[f"{randint(1, 10)}"]
	# global rasmni_korsatish	
	new_photo = open(f'media/photo_redaktor_1/{message.from_user.id}_{tr_1}.jpg', 'rb')
	global rasmni_korsatish
	rasmni_korsatish = await bot.send_photo(chat_id=message.from_user.id,photo=new_photo,caption=caption, reply_markup=rasmni_korish(jami_nomli, call_1, call_2, check))
	# try:
	# 	os.remove(f'media/photo/8-mart/{message.from_user.id}_{tr_1}.jpg')
		
	# except Exception as e:
	# 	print("birinchida xato")
    # await state.set_state("send_users")





@dp.callback_query_handler(text="oldinga_8-mart_1")
async def change_(call: CallbackQuery):
	# await call.message.delete()
	# print("2")

	global tr_1
	tr_1 += 1

	if tr_1>jami_nomli:
		tr_1 -= 1
		await call.answer("Bu oxirgi rasm")
	else:
		# await call.message.answer_photo(photo=open(f"media/photo/8-mart{tr_1}.jpg","rb"), caption=f"O'zingizga yoqqan rasmni tanlang", reply_markup=change_photo(tr_1))
		try:
			global caption
			caption = sherlar[f"{randint(1, 10)}"]
			ism_ = ism
			# rasm_qayta_ishla(call.from_user.id, ism)
			global rasmni_korsatish
			new_photo = open(f'media/photo_redaktor_1/{call.from_user.id}_{tr_1}.jpg', 'rb')
			rasmni_korsatish =  await bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption), chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=change_photo(tr_1, jami_nomli, call_1, call_2, check))	
			
		except Exception as e:
			pass
		# try:
			
		# 	os.remove(f'media/photo/8-mart/{call.from_user.id}_{tr_1}.jpg')
		# except Exception as e:
		# 	print("oldinga xato")

		# await call.message.edit_media(media=open('media/photo/8-mart3.jpg', 'rb') )




@dp.callback_query_handler(text="ortga_8-mart_1")
async def change_(call: CallbackQuery):
	# await call.message.delete()
	global tr_1
	tr_1 -= 1
	# print("ortga ism yozilgan")

	if tr_1 == 0:
		tr_1 += 1
		await call.answer("Bu birinchi rasm")
	else:
		# await call.message.answer_photo(photo=open(f"media/photo/8-mart{tr_1}.jpg","rb"), caption=f"O'zingizga yoqqan rasmni tanlang", reply_markup=change_photo(tr_1))

		
		global caption
		caption = sherlar[f"{randint(1, 10)}"]
		ism_ = ism

		# rasm_qayta_ishla(tr_1, call.from_user.id, ism)
		new_photo = open(f'media/photo_redaktor_1/{call.from_user.id}_{tr_1}.jpg', 'rb')
		global rasmni_korsatish
		rasmni_korsatish = await bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption), chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=change_photo(tr_1, jami_nomli, call_1, call_2, check))	
		# try:
		# 	os.remove(f'media/photo/8-mart/{call.from_user.id}_{tr_1}.jpg')
		# except Exception as e:
		# 	print("ortga xato")


@dp.callback_query_handler(text="place")
async def change_(call: CallbackQuery):
	# await call.message.delete()
	
	await call.answer(f"Bu {tr_1} - rasm")
	




@dp.callback_query_handler(text="8-mart-ismli")
async def check(call: CallbackQuery):

	########### eski rasmlarini ochiradi #############
	# await call.message.delete()
	
	# await call.answer(f"{tr_1} - rasm")
	rek = f"\n🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n🌺 8- mart 'Xalqaro xotin-qizlar kuni' bayrmi bilan tabriklayman! 🌷 Doimo yuzingizdan kulgu, labingizdan tabassum, ko'zlaringizdan esa baxt uchqunlari arimasin. 💐"
	rek += "🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n\n@tabriknoma_yasovchi_bot"
	caption_ = caption + rek

	# rasm_qayta_ishla(tr_1, call.from_user.id, ism)
	new_photo = open(f'media/photo_redaktor_1/{call.from_user.id}_{tr_1}.jpg', 'rb')
	# print(rasmni_korsatish)
	# await rasmni_korsatish.delete()
	await bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption_), chat_id=call.message.chat.id, message_id=call.message.message_id)	

	try:
		idl = call.from_user.id
		for i in range(1,14):
			path = str(idl)+"_"+str(i)+".jpg"
			os.unlink(f"media/photo_redaktor_1/{path}")
		
	except Exception as e:
		# print(e)
		pass
	# os.remove(f'media/photo/8-mart/{call.from_user.id}_{tr_1}.jpg')
	


@dp.callback_query_handler(text="8-mart-ismsiz")
async def check(call: CallbackQuery):
	# await call.message.delete()
	
	# await call.answer(f"{tr_1} - rasm")
	rek = "\n🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n🌺 8- mart 'Xalqaro xotin-qizlar kuni' bayrmi bilan tabriklayman! 🌷 Doimo yuzingizdan kulgu arimasin. 💐"
	rek += "🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 🌸 🌹 \n\n@tabriknoma_yasovchi_bot"
	caption_ = caption + rek


	new_photo = open(f'media/photo/8-mart/nomsiz_{tr_1}.jpg', 'rb')
	await bot.edit_message_media(media=InputMedia(type='photo', media=new_photo, caption = caption_), chat_id=call.message.chat.id, message_id=call.message.message_id)	





# users = db.select_all_users()
# for user in users:
# 	vaqti_tugash = (datetime.now()+timedelta(minutes=1)).strftime("%X")
# 	date_update = user[2]
# 	if str(date_update) > vaqti_tugash:
# 		print(vaqti_tugash)



