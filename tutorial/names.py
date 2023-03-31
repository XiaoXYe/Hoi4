import os
import re
import shutil
test_path = "D:\\hoi4mod\\test"
ins_path = "C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\tutorial\\"
path = 'C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\'

sub_path = 'gfx\\flags\\'

scaleList = ['\\', 'medium\\', 'small\\']
keyList = ['SHX', 'SAX', 'TIB', 'HUN', 'YUN', 'HAN', 'MAC']
idealogyList = ['communism', 'democratic', 'fascism', 'neutrality']

for scale in scaleList:
    for key in keyList:
        for idealogy in idealogyList:
            old_path = path + sub_path + scale + key + '.tga'
            new_path = path + sub_path + scale + key + '_' + idealogy + '.tga'
            shutil.copyfile(old_path,new_path) # 复制并重命名