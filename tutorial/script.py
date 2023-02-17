import os
import re
test_path = "D:\\hoi4mod\\test"
path = 'C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\history\\states'
ins_path = "C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\tutorial\\instruction.txt"
test_lcl_path = "D:\\hoi4mod\\r_victory_points_l_english.yml"
lcl_path = 'C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\localisation\\english\\replace\\r_victory_points_l_english.yml'
dict = {}
cityLvDict = {
    '0': ['megalopolis', '50', '5', '3', '6'], 
    '1': ['metropolis', '30', '4', '3', '5'], 
    '2': ['large_city', '20', '3', '2', '4'], 
    '3': ['city', '15', '3', '1', '2'], 
    '4': ['large_town', '10', '2', '1', '1'], 
    '5': ['town', '5', '2', '0', '1'], 
    '6': ['rural', '1', '1', '0', '0']
}

str =  '\t\tvictory_points = { 2842 10 }\n\t\tbuildings = {\n\t\t\tinfrastructure = 2\n\t\t\tarms_factory = 1\n\t\t\tindustrial_complex = 1\n\t\t}\n\t}\n}\n'
vpstr = '\t\tvictory_points = {{ {a} {b} }}\n'
bdstr = '\t\tbuildings = {{\n\t\t\tinfrastructure = {a}\n\t\t\tarms_factory = {b}\n\t\t\tindustrial_complex = {c}\n\t\t}}\n'
endstr = '\t}\n}\n'
for file_name in os.listdir(path):
    index = file_name.split('-')[0]
    dict[index] = path + "\\" + file_name
    # print(dict)

lcl_data = 'l_english:\n VICTORY_POINTS_TOOLTIP:0 \"§G$NAME$§!的胜利点值为§Y$POINTS$§!\"\n'
lclstr = ' VICTORY_POINTS_{a}:0 \"{b}\"\n'

with open(ins_path, 'r', encoding='utf-8') as insFile:
    for line in insFile:
        data_line = line.strip("\n").split()
        print(data_line)
        if len(data_line) == 4:
            index = data_line[0]
            nameCN = data_line[1]
            cityLvKey = data_line[2]
            vpProv = data_line[3]
            file_path = dict[index]

            state_category = cityLvDict[cityLvKey][0]
            vp_num = cityLvDict[cityLvKey][1]
            infraLv = cityLvDict[cityLvKey][2]
            afLv = cityLvDict[cityLvKey][3]
            cfLv = cityLvDict[cityLvKey][4]

            rewrite_data = ""
            lcl_data += lclstr.format(a = vpProv, b = nameCN)
            with open(file_path, 'r', encoding='utf-8') as stateFile:
                state_data = stateFile.readlines()
                for line in state_data:
                    rewriteline = line
                    if re.match('\tstate_category', line):
                        rewriteline = '\tstate_category = ' + state_category + '\n'
                    elif re.match('\t\towner', line):
                        rewrite_data += rewriteline
                        break
                    rewrite_data += rewriteline
                rewrite_data += vpstr.format(a = vpProv, b = vp_num)
                rewrite_data += bdstr.format(a = infraLv, b = afLv, c = cfLv)
                rewrite_data += endstr
                print(rewrite_data)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(rewrite_data)
print(lcl_data)
with open(lcl_path, 'w', encoding='utf-8-sig') as f:
    f.write(lcl_data)