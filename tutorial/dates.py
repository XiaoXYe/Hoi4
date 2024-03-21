import os
import re
import shutil
test_path = "path = 'C:\\Hoi4Mod\\Hoi4\\tutorial\\test\\"
ins_path = "C:\\Hoi4Mod\\Hoi4\\tutorial\\"
path = 'C:\\Hoi4Mod\\Hoi4\\tutorial\\'

sub_path = 'technologies\\'

old_date = ["1918", "1936", "1937", "1938", "1939", "1940", "1941", "1942", "1943", "1944", "1945"]
new_date = ["2002", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029"]

fileNameList = os.listdir(path + sub_path)
print(fileNameList)
for file_name in fileNameList:
	new_tech_data = ''
	with open(path + sub_path + file_name, 'r', encoding='utf-8') as techFile:
		tech_data = techFile.readlines()
		for data in tech_data:
			for i in range(11):
				data = data.replace(old_date[i], new_date[i])
			new_tech_data += data
	with open(test_path + file_name, 'w', encoding='utf-8') as techFile:
		techFile.write(new_tech_data)