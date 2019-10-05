#PROJECT: JPG TO ASCII IMAGE CONVERTER
#CREATOR: GABRIEL SMITH
#LIBRARIES USED: NUMPY, PILLOW
#DATE: 10/4/2019

import PIL
import numpy as np
from PIL import Image 

#row = height
#col = width
# -------------------------- GLOBAL VALUES ------------------------------


ascii_string = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
pixel = np.array([])
outputBuffer = ""

def imageOpen():
	image = Image.open('images\img1.jpg')
	return image

# -------------------------- IMAGE PROCESSING --------------------------
def pixelProcess(count, row, col,brightnessBuffer,image):
	im_data = np.array(image)
	pixel = im_data[row][col]
	new_arr = ""
	brightnessBuffer[count] = (0.21*pixel[0])+(0.72*pixel[1])+(0.07*pixel[2])
	ascii_conv = int(brightnessBuffer[count]/4)
	new_arr += ascii_string[ascii_conv]
	return new_arr

# -------------------------- MAIN PROCEDURE -----------------------------

if __name__ == '__main__':
	try:
		image = imageOpen()
		print('Successfully loaded image!')

		brightnessBuffer = np.empty([image.size[0]*image.size[1]])
		i,x,y = 0,0,0
		width, height = image.size
		ascii_image = np.array([])		

		for x in range(height):
			for y in range(width):
				if(y%width==0):
					outputBuffer+='\n'
				outputBuffer+=pixelProcess(i,x,y,brightnessBuffer,image)

				i+=1
		print(outputBuffer)
		output_file = open("sampleOutput.txt", "w")
		output_file.write(outputBuffer)
		output_file.close()		
	except IOError:
		print('An error occured when attempting to open the file.')


