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


