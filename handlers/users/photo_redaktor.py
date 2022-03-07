
from PIL import Image, ImageFont, ImageDraw
import os

###################   8- mart uchun ism yoziladigan  bolim ###############333
###################   8- mart uchun ism yoziladigan  bolim ###############333
async def rasm_qayta_ishla(user_id, ism):
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
	# img.show()

# # elif tr == 2:

# 	img = Image.open(f"media/photo/8-mart/nomli_{tr}.jpg")

# 	font = ImageFont.truetype("media/fonts/ANTQUABI.ttf", 102)  ## impact, arial
# # font = ImageFont.truetype("resources/HelveticaNeueLight.ttf", fontsize)
# 	draw = ImageDraw.Draw(img)

# 	draw.text((570,100), ism, (25,0,30), font=font)
# 	# draw.text((640,475), iftor, (0,190,120), font=font2)

# 	img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

# 	# img.show()

# # elif tr == 3:

# 	img = Image.open(f"media/photo/8-mart/nomli_{tr}.jpg")

# 	font = ImageFont.truetype("media/fonts/Gstswzrm.ttf", 65)  ## impact, arial
# # font = ImageFont.truetype("resources/HelveticaNeueLight.ttf", fontsize)
# 	draw = ImageDraw.Draw(img)

# 	draw.text((330,620), "Bayramingiz bilan "+ism, (55,190,30), font=font)
# 	# draw.text((640,475), iftor, (0,190,120), font=font2)

# 	img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

# 	# img.show()

# # elif tr == 4:
# 	img = Image.open(f"media/photo/8-mart/nomli_{tr}.jpg")
	
# 	font = ImageFont.truetype("media/fonts/BRITANIC.ttf", 105)  ## impact, arial

# 	draw = ImageDraw.Draw(img)

# 	draw.text((700,80), ism, (55,190,30), font=font)
	

# 	img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

# 	# img.show()

# # elif tr == 5:
# 	img = Image.open(f"media/photo/8-mart/nomli_{tr}.jpg")
		
# 	font = ImageFont.truetype("media/fonts/Gstswzrm.ttf", 80)  ## impact, arial

# 	draw = ImageDraw.Draw(img)

# 	draw.text((380,110), ism, (55,190,30), font=font)
	

# 	img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

# 	# img.show()


# # elif tr == 6:
# 	img = Image.open(f"media/photo/8-mart/nomli_{tr}.jpg")
		
# 	font = ImageFont.truetype("media/fonts/Gstswzrm.ttf", 40)  ## impact, arial

# 	draw = ImageDraw.Draw(img)

# 	draw.text((230,55), ism, (25,220,150), font=font)
	

# 	img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

# 	# img.show()

# # elif tr == 7:
# 	img = Image.open(f"media/photo/8-mart/nomli_{tr}.jpg")
	
# 	font = ImageFont.truetype("media/fonts/BRITANIC.ttf", 95)  ## impact, arial

# 	draw = ImageDraw.Draw(img)

# 	draw.text((70,75), ism, (255,10,10), font=font)
	

# 	img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

# 	# img.show()

# # elif tr == 8:
# 	img = Image.open(f"media/photo/8-mart/nomli_{tr}.jpg")
	
# 	font = ImageFont.truetype("media/fonts/Gstswzrm.ttf", 50)  ## impact, arial

# 	draw = ImageDraw.Draw(img)

# 	draw.text((180,185), ism, (155,0,0), font=font)
	

# 	img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

# 	# img.show()

# # elif tr == 9:
# 	img = Image.open(f"media/photo/8-mart/nomli_{tr}.jpg")
	
# 	font = ImageFont.truetype("media/fonts/TR Kastler Bold Italik.ttf", 100)  ## impact, arial

# 	draw = ImageDraw.Draw(img)

# 	draw.text((175,145), ism, (255,20,150), font=font)
	

# 	img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

# # elif tr == 10:
# 	img = Image.open(f"media/photo/8-mart/nomli_{tr}.jpg")
	
# 	font = ImageFont.truetype("media/fonts/TR Renfrew.ttf", 40)  ## impact, arial

# 	draw = ImageDraw.Draw(img)

# 	draw.text((55,65), ism, (255,100,0), font=font)
	

# 	img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

# # elif tr == 11:
# 	img = Image.open(f"media/photo/8-mart/nomli_{tr}.jpg")
	
# 	font = ImageFont.truetype("media/fonts/HARLOWSI.ttf", 45)  ## impact, arial

# 	draw = ImageDraw.Draw(img)

# 	draw.text((40,45), ism, (0,255,0), font=font)
	

# 	img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

# # elif tr == 12:
# 	img = Image.open(f"media/photo/8-mart/nomli_{tr}.jpg")
	
# 	font = ImageFont.truetype("media/fonts/HARLOWSI.ttf", 105)  ## impact, arial

# 	draw = ImageDraw.Draw(img)

# 	draw.text((120,75), ism, (0,255,0), font=font)
	

# 	img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")

# # elif tr == 13:
# 	img = Image.open(f"media/photo/8-mart/nomli_{tr}.jpg")
	
# 	font = ImageFont.truetype("media/fonts/HARLOWSI.ttf", 105)  ## impact, arial

# 	draw = ImageDraw.Draw(img)

# 	draw.text((230,345), ism, (90,50,0), font=font)
	

# 	img.save(f"media/photo/8-mart/{user_id}_{tr}.jpg")
