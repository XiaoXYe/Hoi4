import os
import re
import shutil
test_path = "D:\\hoi4mod\\test"
ins_path = "C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\tutorial\\"
path = 'C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\'

sub_path = 'common\\technologies\\'

origin_date_list = []
for i in range(1918, 1956):
	origin_date_list.append(str(i))
delta = 84

print(origin_date_list)
for file_name in os.listdir(path + sub_path):
	technology_content = ''
	with open(path + sub_path + file_name, 'r', encoding='utf-8-sig') as technologyFile:
		technology_data = technologyFile.readlines();
		for line in technology_data:
			new_line = line
			for origin_date in origin_date_list:
				target_date = str(int(origin_date) + delta)
				new_line = new_line.replace(origin_date, target_date)
			technology_content += new_line
	with open(path + sub_path + file_name, 'w', encoding='utf-8') as technologyFile:
		technologyFile.write(technology_content)