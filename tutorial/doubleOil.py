import os
import re
import shutil
test_path = "D:\\hoi4mod\\test"
ins_path = "C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\tutorial\\"
path = 'C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\'

sub_path = 'history\\states\\'

for file_name in os.listdir(path + sub_path):
	state_content = ''
	flag = False
	with open(path + sub_path + file_name, 'r', encoding='utf-8') as stateFile:
		state_data = stateFile.readlines();
		for line in state_data:
			new_line = line
			if re.match('\t\toil', line):
				flag = True
				oilNum = new_line.split('=')[1].split(' ')[1].split('\n')[0]
				print(oilNum)
				oilNum = str(int(oilNum) * 2)
				new_line = '\t\toil = ' + oilNum + '\n'
			state_content += new_line
	if flag:
		print(state_content)
		with open(path + sub_path + file_name, 'w', encoding='utf-8') as stateFile:
			stateFile.write(state_content)