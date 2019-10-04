import PIL
import numpy as np
from PIL import Image 

bright_max = np.array([])
#print image funciton

def show():
	image.show()

#grab information such as width, height, etc.
def imageProcess(width, height):

	pixel = np.array([],[])
	new_array = np.array([])
	print("Width:", width, "\nHeight:", height)
	#load the jpg information into a 2d numpy array
	im_data = np.array(image)

	#iterate through pixel data
	for x in range(height-1):
		for y in range(width-1):
			pixel = im_data[x][y]
			bright_max = (0.2126*pixel[0]) + (0.7152*pixel[1])+(0.0722*pixel[2])
			print(bright_max)
		return np.prod(bright_max.shape)



if __name__ == '__main__':
	#read in the image and display the image. 
	try:
		image = Image.open('images\img1.jpg')
		width, height = image.size		
		print('Successfully loaded image!')
		print(imageProcess(width, height))
		#for i in len(bright_max):
			#print(bright_max[i])		
	except IOError:
		print('An error occured trying to open the file.')


