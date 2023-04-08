import os
import re
import shutil
test_path = "D:\\hoi4mod\\test"
ins_path = "C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\tutorial\\"
path = 'C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\'

sub_path = 'history\\states\\'

addList = []
for file_name in os.listdir(path + sub_path):
	state_content = ''
	addFlag = True
	with open(path + sub_path + file_name, 'r', encoding='utf-8') as stateFile:
		state_data = stateFile.readlines();
		for line in state_data:
			new_line = line
			if re.match('\thistory', line):
				addFlag = False
			if re.match('}', line) and addFlag:
				addList.append(file_name)
				new_line = '\thistory = {\n\t\tadd_core_of = TST\n\t\towner = TST\n\t}\n}'
			state_content += new_line
	if addFlag:
		print(state_content)
	with open(path + sub_path + file_name, 'w', encoding='utf-8') as stateFile:
		stateFile.write(state_content)
print(addList)