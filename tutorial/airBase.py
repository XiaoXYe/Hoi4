import os
import re
test_path = "D:\\hoi4mod\\test"
path = 'C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\history\\states'
ins_path = "C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\tutorial\\"
dict = {}
air_categories = ['AirBase']
for file_name in os.listdir(path):
    index = file_name.split('-')[0]
    dict[index] = path + "\\" + file_name
    # print(dict)

airBase_key = '\t\t\tair_base'
history_key = '\thistory'
buildings_key = '\t\tbuildings'
industrial_complex_key ='\t\t\tindustrial_complex'
infrastructure_key = '\t\t\tinfrastructure'
lv5_key = '\tstate_category = megalopolis'
lv4_key = '\tstate_category = metropolis'
lv3_key = '\tstate_category = large_city'
lv2_key = '\tstate_category = city'
lv1_key = '\tstate_category = large_town'
lv0_key = '\tstate_category = town'
for air_category in air_categories:
    airBaseStr = '\t\t\tair_base = {a}\n'
    with open(ins_path + air_category + '.txt', 'r', encoding='utf-8') as insFile:
        for line in insFile:
            data_line = line.strip("\n").split()
            print(data_line)
            if len(data_line) >= 1:
                index = data_line[0]
                lv = 0
                hasAirBase = False
                if index[0] >='0' and index[0] <= '9':
                    file_path = dict[index]
                    with open(file_path, 'r', encoding='utf-8') as stateFile:
                        state_data = stateFile.readlines()
                        for line in state_data:
                            if re.match(lv5_key, line):
                                lv = 10
                            elif re.match(lv4_key, line):
                                lv = 8
                            elif re.match(lv3_key, line):
                                lv = 6
                            elif re.match(lv2_key, line):
                                lv = 4
                            elif re.match(lv1_key, line):
                                lv = 2
                            elif re.match(lv0_key, line):
                                lv = 1
                            elif re.match(airBase_key, line):
                                hasAirBase = True
                    rewrite_data = ""
                    with open(file_path, 'r', encoding='utf-8') as stateFile:
                        state_data = stateFile.readlines()
                        if hasAirBase:
                            for line in state_data:
                                rewriteline = line
                                if re.match(airBase_key, line):
                                    rewriteline = airBaseStr.format(a = lv)
                                rewrite_data += rewriteline
                        else:
                            for line in state_data:
                                rewriteline = line
                                if re.match(infrastructure_key, line):
                                    rewriteline = line + airBaseStr.format(a = lv)
                                rewrite_data += rewriteline
                    print(rewrite_data)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(rewrite_data)