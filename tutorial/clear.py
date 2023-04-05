import os
import re
import shutil
test_path = "D:\\hoi4mod\\test"
ins_path = "C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\tutorial\\"
path = 'C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\'

sub_path = 'tutorial\\clear\\'

for file_name in os.listdir(path + sub_path):
	clear_content = ''
	with open(path + sub_path + file_name, 'w', encoding='utf-8') as clearFile:
		clearFile.write(clear_content)