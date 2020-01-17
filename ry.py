from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

img = Image.open("img1.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Roboto-Regular.ttf", 25)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((0, 0),"Sample Text",(255,255,255),font=font)
img.save('sample-out.jpg')

