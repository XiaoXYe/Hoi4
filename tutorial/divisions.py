import os
import re
import shutil
test_path = "D:\\hoi4mod\\test"
ins_path = "C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\tutorial\\"
path = 'C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\'

template_path = 'history\\units\\GEN.txt'
template_str = '\t\tlocation = {a}\n'
keyList = []
key_path = 'history\\countries\\'
for file_name in os.listdir(path + key_path):
    tag = file_name.split('-')[0].split(' ')[0]
    if tag == 'TST':
        continue
    print(tag)
    capital = ''
    country_content = ''
    oob_str = 'oob = \"{}\"\n'
    with open(path + key_path + file_name, 'r', encoding='utf-8-sig') as countryFile:
        country_data = countryFile.readlines()
        for line in country_data:
            if re.match('capital', line):
                capital = line.split('=')[1].split(' ')[1].split('\n')[0]
                country_content += line + oob_str.format(tag)
                continue
            if re.match('\ufeffcapital', line):
                capital = line.split('=')[1].split(' ')[1].split('\n')[0]
                country_content += line + oob_str.format(tag)
                continue
            country_content += line
    #print(country_content)
    with open(path + key_path + file_name, 'w', encoding='utf-8-sig') as f:
        f.write(country_content)

    print(capital)
    state_path = 'history\\states\\'
    provinceID = ' '
    for stateFile_name in os.listdir(path + state_path):
        stateID = stateFile_name.split('-')[0]
        if stateID == capital:
             with open(path + state_path + stateFile_name, 'r', encoding='utf-8') as stateFile:
                state_data = stateFile.readlines()
                # print(state_data)
                thisIsTheLine = False
                for line in state_data:
                    if thisIsTheLine:
                        provinceID = line.split('\t')[-1].split('\n')[0].split(' ')[0]
                        break
                    if re.match('\tprovinces', line):
                        thisIsTheLine = True
                        continue
        if provinceID != ' ':
            break
    print(provinceID)
    oob_content = ''
    with open(path + template_path, 'r', encoding='utf-8-sig') as templateFile:
        template_data = templateFile.readlines()
        for line in template_data:
            if re.match('\t\tlocation', line):
                oob_content += template_str.format(a = provinceID)
            else:
                oob_content += line
    with open(path + 'history\\units\\' + tag + '.txt', 'w', encoding='utf-8-sig') as f:
        f.write(oob_content)