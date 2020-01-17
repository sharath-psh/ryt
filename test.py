from PIL import ImageDraw, ImageFont, Image

# parameters
text = "Sample Text"
selected_font = "Roboto-Regular.ttf"
font_size = 30

# get the size of the text
img = Image.open("img1.jpg")
font = ImageFont.truetype(selected_font, font_size)
draw = ImageDraw.Draw(img)
text_size = draw.textsize(text, font)

# resize and draw
img = img.resize(text_size)
draw.text((0,0), text, (0,0,0), font)
img.save('signature.png')