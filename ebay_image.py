from I_handling import *
import sys

def main(m_dir, target_dir, x_y):
	if type(x_y) != tuple:
		return "x_y must be a tuple containing the desired width and height of the new image(s)"
	cur_contents = dir_grab(m_dir)
	for i in range(0, len(cur_contents)):
		new_name = target_dir + '\\' + cur_contents[i]
		I_handling(m_dir + '\\'+ cur_contents[i] ).resize(x_y, new_name)
		print("Saved {0}".format(new_name))
	return "Complete"



if len(sys.argv) > 1:
	main(sys.argv[1], sys.argv[2], sys.argv[3])
else:
	print('[directory containing the images] [directory where you want the new images to go] [new size of images]')