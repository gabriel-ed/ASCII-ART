import PIL
from PIL import Image
#print image funciton
def show():
	image.show()

#grab information such as width, height, etc.
def grabInfo():
	width, height = image.size
	print("Width:", width, "\nHeight:", height)







if __name__ == '__main__':

	#read in the image and display the image. 
	try:
		image = Image.open('images\img1.jpg')
		print('Successfully loaded image!')
		grabInfo()
	except IOError:
		print('An error occured trying to open the file.')


