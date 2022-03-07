# from PIL import Image, ImageFont, ImageDraw

# img = Image.open("media/photo/8-mart/nomli_3.jpg")
# # font1 = ImageFont.truetype("media/fonts/HARLOWSI.ttf", 105)  ## impact, IthornЙt.ttf
# # # font2 = ImageFont.truetype("Warnock Pro SmBd Display.ttf", 100)  ## impact, "media/fonts/ANTQUABI.ttf"

# # draw = ImageDraw.Draw(img)

# text = "Bayramingiz"
# date = "bilan"
# ism = "Mamalakat"
# iftor = ""


# font = ImageFont.truetype("media/fonts/Gstswzrm.ttf", 225)  ## impact, arial
# # font = ImageFont.truetype("resources/HelveticaNeueLight.ttf", fontsize)
# draw = ImageDraw.Draw(img)

# draw.text((2600,1890), ism, (55,190,30), font=font)
# # draw.text((640,475), iftor, (0,190,120), font=font2)

# # img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")



# # draw.text((50,52), text, (0,0,0), font=font1)
# # draw.text((400,160), date, (0,0,80), font=font2)
# # draw.text((230,345), ism, (90,50,0), font=font1)
# # draw.text((640,475), iftor, (0,190,120), font=font2)

# # img.save("newImage.jpg")

# img.show()

# # from random import randint
# # print(randint(1, 10))




# ######################fayllar bilan ishlash ##################################
# ######################fayllar bilan ishlash ##################################
# ######################fayllar bilan ishlash ##################################

import os
import shutil
# os.mkdir("media/photo_redaktor_1")  #### yangi papka yaratadi
# # # os.rmdir("newFolder")    ###  bo'sh papkani ochiradi
# shutil.rmtree("media/photo_redaktor_1/")   ### ko'rsatilgan papkani barcha ma'lumotlari bilan ochiradi
# os.remove("media/photo_redaktor_1/*.*")   ### ko'rsatilgan faylni ochiradi  

# # ###################################
# file = 'media/photo_redaktor_1/new_txt5.txt' ##### yangi fayl yaratadi
# a=open(file, 'a') 
# # # ##### 'a' -> 'append' oldingi faylga qo'shimcha qo'shish uchun ochadi
# # # ##### 'w' -> 'write' oldingi matnni ochirib faylni ochadi
# # # print(a)
# a.write("\nnew code new code new code new code new code new code new code new code new code ")  ### fayl ichiga yozadi
# a.close()
# # # ###################################


#######################33 berilgan papkadagi hamma malumotni ochiradi##############33
# import os, shutil
# folder = "media/photo_redaktor_1"
# for filename in os.listdir(folder):
#     file_path = os.path.join(folder, filename)
#     try:
#         if os.path.isfile(file_path) or os.path.islink(file_path):
#             os.unlink(file_path)
#         elif os.path.isdir(file_path):
#             shutil.rmtree(file_path)
#     except Exception as e:
#         print('Failed to delete %s. Reason: %s' % (file_path, e))



# # ########################   korsatilgan malumotlarni ochiradi
# idl = "973108256_"
# for i in range(1,14):
# 	path = idl+str(i)+".jpg"
# 	os.unlink(f"media/photo_redaktor_1/{path}")




####################### timedelta ishlatilishi
# from datetime import datetime, timedelta


# vaqti = datetime.now().strftime("%X")
# print(vaqti)
# print(datetime.now().strftime("%H:%M:%S %p"))
# print((datetime.now() + timedelta(minutes=5)).strftime("%X"))