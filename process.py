import PIL
import numpy as np
from PIL import Image 
#print image funciton

pixel = np.array([],[])
def show():
	image.show()

#grab information such as width, height, etc.
def imageProcess():
	width, height = image.size
	bright_max = []
	print("Width:", width, "\nHeight:", height)
	#load the jpg information into a 2d numpy array
	im_data = np.array(image)
	#iterate through pixel data
	for x in range(width):
		for y in range(height):
			pixel = im_data[x][y]
			bright_max.append((pixel[0]+pixel[1]+pixel[2])/3)
			print(pixel)
			print("Brightness avg:", bright_max[y])
	return 



if __name__ == '__main__':
	#read in the image and display the image. 
	try:
		image = Image.open('images\img1.jpg')
		print('Successfully loaded image!')
		imageProcess()
	except IOError:
		print('An error occured trying to open the file.')


