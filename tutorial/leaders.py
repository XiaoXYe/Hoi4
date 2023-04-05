import os
import re
import shutil
test_path = "D:\\hoi4mod\\test"
ins_path = "C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\tutorial\\"
path = 'C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\'

sub_path1 = 'gfx\\leaders\\PRC\\'
sub_path2 = 'history\\countries\\'
scaleList = ['\\', 'medium\\', 'small\\']
keyList = ['SHX', 'SAX', 'TIB', 'HUN', 'YUN', 'HAN', 'MAC']
idealogyList = ['communism', 'democratic', 'fascism', 'neutrality']

d = dict()

for file_name in os.listdir(path + sub_path1):
	state = file_name.split('_')[1]
	d[state] = file_name

for file_name in os.listdir(path + sub_path2):
	state = file_name.split('.')[0].split('-')[1].split(' ')[1]
	if state == 'Test':
		continue
	technology_content = ''
	with open(path + sub_path2 + file_name, 'r', encoding='utf-8-sig') as technologyFile:
		technology_data = technologyFile.readlines();
		for line in technology_data:
			new_line = line
			new_line = new_line.replace("GFX_Portrait_Asia_Generic_1", "\"gfx/leaders/PRC/" + d[state] + "\"")
			technology_content += new_line
	with open(path + sub_path2 + file_name, 'w', encoding='utf-8-sig') as technologyFile:
		technologyFile.write(technology_content)