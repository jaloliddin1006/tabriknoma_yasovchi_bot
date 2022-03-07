import asyncio

from aiogram import types, utils
from aiogram.types import ReplyKeyboardRemove

from data.config import ADMINS, GROUP_CHAT_ID
from loader import dp, db, bot
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):

    users = len(db.select_all_users())
    await message.answer(f"Botdan fodyalanuvchilar soni: {users}")





@dp.message_handler(text="/reklama", user_id=ADMINS, state=None)
async def send_ad_to_all(message: types.Message, state=FSMContext):
    try:
        await message.answer("✅ Reklamani botga forward qiling. Siz forward qilgan reklama to'gridan to'g'ri barcha foydalanuchilarga yuboriladi. \n\n✅ Yoki xabar matnini kiriting: \n\n⚠️ Xabar yuborishni istamasangiz /bekor kamandasini kiriting.", reply_markup=ReplyKeyboardRemove())
        # print("1")
    except Exception as e:
        await message.answer("✅ Reklamani botga forward qiling. Siz forward qilgan reklama to'gridan to'g'ri barcha foydalanuchilarga yuboriladi. \n\n✅ Yoki xabar matnini kiriting: \n\n⚠️ Xabar yuborishni istamasangiz /bekor kamandasini kiriting.")
        # print("2")
        

    await state.set_state("send_users")



@dp.message_handler(state="send_users", text="/bekor")
async def send_ad_to_all(message: types.Message, state=FSMContext):
    await message.answer("❌ Bekor qilindi")
    await state.finish()
 


@dp.message_handler(state="send_users", content_types="text", is_forwarded=False)
async def send_ad_to_all(message: types.Message, state=FSMContext):
    await state.finish()
    bloklaganlar = 0
    jonlilar = 0

    users = db.select_all_users()
    # print(message)
    # print(message.forward_from_message_id)
    # print(message.forward_from.id)
    for user in users:
        user_id = user[0]
        # print(message.message_id)

        try:
            # await message.answer(user_id,  message.text ) 
            await bot.send_message(user_id, message.text) 
            # print(jonlilar)
            jonlilar += 1
            # print("user's msg")
        except utils.exceptions.BotBlocked as e:
            bloklaganlar += 1
            # print("blok")
            
        except:
            pass
        #     await message.forward(user_id, message.forward_from_chat.id, message.forward_from_message_id ) 
            # print("channel's msg")

        else:
            pass


        # print("yes")
        await asyncio.sleep(0.05)
    await message.answer("✅ Xabaringiz foydalanuvchilarga yetkazildi...")
    await message.answer(f"Jami foydalanuvchilar soni: {bloklaganlar+jonlilar}")
    await message.answer(f"Bloklagan foydalanuvchilar soni: {bloklaganlar}")
    await message.answer(f"Faol foydalanuvchilar soni: {jonlilar}")

 

@dp.message_handler(state="send_users", content_types="any", is_forwarded=True)
async def send_ad_to_all(message: types.Message, state=FSMContext):
    await state.finish()
  
    bloklaganlar = 0
    jonlilar = 0

    users = db.select_all_users()
    # print(message)
    # print(message.forward_from_message_id)
    # print(message.forward_from.id)
    for user in users:
        user_id = user[0]
        # print(message.message_id)

        try:
            await message.forward(user_id, message.forward_from.id, message.forward_from_message_id ) 
            # print("user's msg")
            jonlilar += 1

        except utils.exceptions.BotBlocked as e:
            # print("blok")
            bloklaganlar += 1

            # pass
        except:
            await message.forward(user_id, message.forward_from_chat.id, message.forward_from_message_id ) 
            # print("channel's msg")
            jonlilar += 1


        else:
            pass


        # print("yes")
        await asyncio.sleep(0.05)


    await message.answer("✅ Xabaringiz foydalanuvchilarga yetkazildi...")

    await message.answer(f"Jami foydalanuvchilar soni: {bloklaganlar+jonlilar}")
    await message.answer(f"Bloklagan foydalanuvchilar soni: {bloklaganlar}")
    await message.answer(f"Faol foydalanuvchilar soni: {jonlilar}")
