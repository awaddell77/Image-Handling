from PIL import Image
import os



class I_handling(object):
	def __init__(self, fname):
		self.fname = str(fname)
		self.image = Image.open(self.fname)
	def resize(self, x_y, new_name=''):
		#x is width
		#y is height
		new_image = self.image.resize(x_y)
		if new_name != '':
			new_image.save(new_name)
			new_image.close()
		else:
			new_image.save(fname)
			new_image.close()

	def close(self):
		print("Closing file: {0}".format(self.fname))
		self.image.close()




def dir_grab(dir_name, target_ext = ''):
	#dir_name must be complete
	#returns a list of all the items in a given directory
	contents = os.listdir(dir_name)
	#if target_ext != '':
	return contents

