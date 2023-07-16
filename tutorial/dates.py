import os
import re
import shutil
test_path = "D:\\hoi4mod\\test"
ins_path = "C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\tutorial\\"
path = 'C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\'

sub_path = 'tutorial\\replace\\'

origin_date_list = []
fileNameList = os.listdir(path + sub_path)
for file_name in fileNameList:
	new_localisation_data = ''
	with open(path + sub_path + file_name, 'r', encoding='utf-8-sig') as localisationFile:
		localisation_data = localisationFile.readlines()
		index = 0
		for data in localisation_data:
			if index == 0:
				data = data.replace("english", "simp_chinese")
			new_localisation_data += data
			index += 1
	with open(path + sub_path + file_name, 'w', encoding='utf-8-sig') as localisationFile:
		localisationFile.write(new_localisation_data)
	new_name = file_name.replace("english", "simp_chinese")
	os.rename(path + sub_path + file_name, path + sub_path + new_name)