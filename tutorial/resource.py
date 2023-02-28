import os
import re
test_path = "D:\\hoi4mod\\test"
path = 'C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\history\\states'
ins_path = "C:\\Users\\JacobXij\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\EastMeme\\tutorial\\"
dict = {}
resource_categories = ['steel', 'oil', 'rubber', 'aluminium', 'tungsten', 'chromium']
for file_name in os.listdir(path):
    index = file_name.split('-')[0]
    dict[index] = path + "\\" + file_name
    # print(dict)

resource_key = '\tresources'
history_key = '\thistory'
for resource_category in resource_categories:
    resource_category_key = '\t\t' + resource_category
    resourceStr = '\t\t{a} = {b}\n'
    fullResourceStr = '\n\tresources = {{\n\t\t{a} = {b}\n\t}}\n\n'
    with open(ins_path + resource_category + '.txt', 'r', encoding='utf-8') as insFile:
        for line in insFile:
            data_line = line.strip("\n").split()
            print(data_line)
            if len(data_line) >= 2:
                index = data_line[0]
                resourceNum = data_line[1]

                if index[0] >='0' and index[0] <= '9':
                    file_path = dict[index]
                    rewrite_data = ""
                    hasResource = False
                    hasResources = False
                    with open(file_path, 'r', encoding='utf-8') as stateFile:
                        state_data = stateFile.readlines()
                        for line in state_data:
                            if re.match(resource_category_key, line):
                                hasResource = True
                            elif re.match(resource_key, line):
                                hasResources = True
                    with open(file_path, 'r', encoding='utf-8') as stateFile:
                        state_data = stateFile.readlines()
                        if hasResource and hasResources:
                            for line in state_data:
                                rewriteline = line
                                if re.match(resource_category_key, line):
                                    rewriteline = resourceStr.format(a = resource_category, b = resourceNum)
                                rewrite_data += rewriteline
                        elif hasResources:
                            for line in state_data:
                                rewriteline = line
                                if re.match(resource_key, line):
                                    rewriteline = line + resourceStr.format(a = resource_category, b = resourceNum)
                                rewrite_data += rewriteline
                        else:
                            for line in state_data:
                                rewriteline = line
                                if re.match(history_key, line):
                                    rewriteline = fullResourceStr.format(a = resource_category, b = resourceNum) + line
                                rewrite_data += rewriteline
                    print(rewrite_data)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(rewrite_data)