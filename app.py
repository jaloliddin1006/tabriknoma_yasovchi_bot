from aiogram import executor
# from pprint import pprint as print

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

## orginal bot token : 5156859808:AAG24km29URU0yDDYeeOBuKkttsqTqS_luc
## token bot for test: 5226692289:AAGqgqjmsnZwGzcGJXr__8rfW3GjGRjA8tA
async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)
    # print("xxxxxxx")
    # Ma'lumotlar bazasini yaratamiz:
    try:
        db.create_table_users()
    except Exception as err:
        pass

    # Bot ishga tushgani haqida adminga xabar berish
    try:
        await on_startup_notify(dispatcher)
        
    except Exception as e:
        print(e)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
