import os
import re
test_path = "D:\\hoi4mod\\test"
path = 'C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\history\\states'
ins_path = "C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\tutorial\\"
dict = {}
naval_categories = ['NavalBase']
for file_name in os.listdir(path):
    index = file_name.split('-')[0]
    dict[index] = path + "\\" + file_name
    # print(dict)

dockyard_key = '\t\t\tdockyard'
history_key = '\thistory'
buildings_key = '\t\tbuildings'
industrial_complex_key ='\t\t\tindustrial_complex'
for naval_category in naval_categories:
    navalBaseStr = '\t\t\t{a} = {{\n\t\t\t\tnaval_base = {b}\n\t\t\t}}\n'
    fullResourceStr = '\n\tresources = {{\n\t\t{a} = {b}\n\t}}\n\n'
    with open(ins_path + naval_category + '.txt', 'r', encoding='utf-8') as insFile:
        for line in insFile:
            data_line = line.strip("\n").split()
            print(data_line)
            if len(data_line) >= 3:
                index = data_line[0]
                province = data_line[1]
                Lv = data_line[2]

                if index[0] >='0' and index[0] <= '9':
                    file_path = dict[index]
                    rewrite_data = ""
                    with open(file_path, 'r', encoding='utf-8') as stateFile:
                        state_data = stateFile.readlines()
                        for line in state_data:
                            rewriteline = line
                            if re.match(industrial_complex_key, line):
                                rewriteline = line + navalBaseStr.format(a = province, b = Lv)
                            rewrite_data += rewriteline
                    print(rewrite_data)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(rewrite_data)