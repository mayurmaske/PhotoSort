import os
import time
import tkinter.filedialog
import shutil
from pathlib import Path
from tkinter import *
from datetime import datetime
from PIL import Image
import calendar

def user_input_selection():
	tkroot = tkinter.Tk()
	tkroot.withdraw()
	src_dir = tkinter.filedialog.askdirectory(parent=tkroot,initialdir=os.getcwd(),title="Please select directory")
	#src_dir = input("Please enter directory path: ")
	return src_dir
	
def get_date_code(src_file):
	try:
		raw_time = Image.open(src_file)._getexif()[36867]
		date_object = datetime.strptime(raw_time,'%Y:%m:%d %H:%M:%S')
		date_code = date_object.strftime('%Y%m%d_%H%M%S') + '_DC'
		#print("DC Date Code: ",date_code)
	
	except:
		epoch_value = int(os.path.getmtime(src_file))
		date_object = datetime.fromtimestamp(epoch_value)
		date_code = date_object.strftime('%Y%m%d_%H%M%S') + '_DM'
		#print("DM Date Code: ",date_code)
		
	return date_code

def create_dir(path_str):
	if not os.path.exists(path_str):
		os.mkdir(path_str)
		#print("Directory created : {}".format(path_str))
		


def main():
	src_dir = user_input_selection()
	dir_list = os.listdir(src_dir)
	i = 1
	l = len(dir_list)
	
	for file in dir_list:
		src_file = os.path.join(src_dir,file)
		date_code = get_date_code(src_file)
		year_dir = os.path.join(src_dir,date_code[:4])
		month_dir = os.path.join(year_dir,calendar.month_abbr[int(date_code[4:6])])
		
		create_dir(year_dir)
		create_dir(month_dir)
		temp_name = month_dir + '\\' + date_code + '_'+ str(file)
		dst_file = os.path.join(src_dir,temp_name)
		#print(dst_file)
		
		shutil.copy(src_file,dst_file)
		print(str(i) + '/' + str(l) + ' ' + date_code)
		i+=1
		

if __name__ == '__main__':
	main()