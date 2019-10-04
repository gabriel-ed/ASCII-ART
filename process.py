import PIL
import numpy as np
from PIL import Image 
#python numpy array [row, col]
#row = height
#col = width
image = Image.open('images\img4.jpg')
ascii_string = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
brightnessBuffer = np.empty([image.size[0]*image.size[1]])
pixel = np.array([])
im_data = np.array(image)
outputBuffer = np.empty([image.size[0]*image.size[1]])
def imageProcess(count, row, col):
	pixel = im_data[row][col]
	brightnessBuffer[count] = (0.21*pixel[0])+(0.72*pixel[1])+(0.07*pixel[2])
	#print(int(brightnessBuffer[count]))
	ascii_conv = int(brightnessBuffer[count]/4)
	outputBuffer[row,col] = ascii_string[ascii_conv]
	return 
if __name__ == '__main__':
	#read in the image and display the image. 
	try:
		i,x,y = 0,0,0

		width, height = image.size
		ascii_image = np.array([])		
		print("Width:", width, "\nHeight:", height)
		print('Successfully loaded image!')
		for x in range(height):
			for y in range(width):
				imageProcess(i,x,y)
				i+=1

		print(outputBuffer)
	except IOError:
		print('An error occured trying to open the file.')


