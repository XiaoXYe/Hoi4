import os
import re


ins_path = 'C:\\Hoi4Mod\\Hoi4\\tutorial\\litpuppet.txt'
file_path1 = "C:\\Hoi4Mod\\Hoi4\\tutorial\\LIT_puppet_china_effect.txt"
file_path2 = "C:\\Hoi4Mod\\Hoi4\\tutorial\\LIT_puppet_china_trigger.txt"

dicisionCategoryStr = 'LIT_core_china_category = {\n'
decisionTemplate0 = '\t{a} = {{ add_core_od_PREV_and_transfer_to_PREV = yes }}\n'
decisionTemplate1 = '\t\t\thas_full_control_of_state = {a}\n'

with open(ins_path, 'r', encoding='utf-8') as insFile:
    rewrite_data_effect = ''
    rewrite_data_trigger = ''
    for line in insFile:
        data_line = line.strip("\n").split()
        if len(data_line) == 1:
            rewrite_data_effect += data_line[0] + '\n'
            rewrite_data_trigger += data_line[0] + '\n'
            
        if len(data_line) > 1:
            state = data_line[0]
            rewrite_data_effect += decisionTemplate0.format(a = state)
            rewrite_data_trigger += decisionTemplate1.format(a = state)

print(rewrite_data_effect)
with open(file_path1, 'w', encoding='utf-8') as f:
    f.write(rewrite_data_effect)

with open(file_path2, 'w', encoding='utf-8') as f:
    f.write(rewrite_data_trigger)