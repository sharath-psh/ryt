import os
import cv2
from PIL import Image

print(os.getcwd())

os.chdir("D:\\Projects\\ryt\\imgs") 
path = "D:\\Projects\\ryt\\imgs"

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir('.'))


for file in os.listdir('.'): 
	im = Image.open(os.path.join(path, file)) 
	width, height = im.size 
	mean_width += width 
	mean_height += height 
	# im.show() # uncomment this for displaying the image 


mean_width = int(mean_width / num_of_images) 
mean_height = int(mean_height / num_of_images) 


for file in os.listdir('.'): 
	if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"): 
		# opening image using PIL Image 
		im = Image.open(os.path.join(path, file)) 

		# im.size includes the height and width of image 
		width, height = im.size 
		print(width, height) 

		# resizing 
		imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS) 
		imResize.save( file, 'JPEG', quality = 95) # setting quality 
		# printing each resized image name 
		print(im.filename.split('\\')[-1], " is resized") 
