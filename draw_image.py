from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def generate_birthday_image():
	img = Image.open("birthday_test.jpg")
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("lobster.otf",50)
	#font = ImageFont.load("arial.pil")
	draw.text((80,20),"Happy Birthday\n Prateek !",(76,191,230),font=font)
	draw.text((80,45),"Prateek !",(76,191,230),font=font)
	img.save('output.jpg')
	img.show()

generate_birthday_image()