import os
import re


ins_path = 'D:\\Hoi4Mod\\Hoi4\\tutorial\\states.txt'
file_path = "D:\\Hoi4Mod\\Hoi4\\tutorial\\LIT_core_china.txt"

dicisionCategoryStr = 'LIT_core_china_category = {\n'
decisionTemplate0 = '\tLIT_core_{a} = {{\n\t\ticon = infiltrate_state\n\t\thighlight_states = {{ highlight_state_targets = {{ state = 167 }} }}\n\t\tallowed = {{\n\t\t\ttag = LIT\n\t\t}}\n\t\tvisible = {{\n\t\t\thas_country_flag = LIT_integrate_china_flag\n\t\t\ttag = LIT\n\t\t\tOR = {{\n'
decisionTemplate1 = '\t\t\t\t{a} = {{ is_fully_controlled_by_ROOT_and_is_not_core_of_ROOT = yes }}\n'
decisionTemplate2 = '\t\t\t}\n\t\t}\n\t\tavailable = {\n'
decisionTemplate3 = '\t\t\thas_full_control_of_state = {a}\n'
decisionTemplate4 = '\t\t}}\n\t\tcost = 75\n\t\tfire_only_once = yes\n\t\tmodifier = {{\n\t\t\tpolitical_power_gain = -0.20\n\t\t}}\n\t\tdays_remove = 90\n\t\tremove_effect = {{\n\t\t\tlog = \"[GetDateText]: [Root.GetName]: Decision remove LIT_core_{a}\"\n'
decisionTemplate5 = '\t\t\t{a} = {{ remove_claim_by_ROOT_and_add_core_of_ROOT = yes }}\n'
decisionTemplate6 = '\t\t}\n\t\tai_will_do = {\n\t\t\tfactor = 1\n\t\t}\n\t}\n\n'

with open(ins_path, 'r', encoding='utf-8') as insFile:
    rewrite_data = dicisionCategoryStr
    name = ''
    state = ''
    decisionStr0 = ''
    decisionStr1 = ''
    decisionStr3 = ''
    decisionStr4 = ''
    decisionStr5 = ''
    for line in insFile:
        data_line = line.strip("\n").split()
        if len(data_line) == 0:
            rewrite_data += decisionStr0
            rewrite_data += decisionStr1
            rewrite_data += decisionTemplate2
            rewrite_data += decisionStr3
            rewrite_data += decisionStr4
            rewrite_data += decisionStr5
            rewrite_data += decisionTemplate6
            decisionStr0 = ''
            decisionStr1 = ''
            decisionStr3 = ''
            decisionStr4 = ''
            decisionStr5 = ''

        if len(data_line) == 1:
            name = data_line[0]
            decisionStr0 = decisionTemplate0.format(a = name)
            decisionStr4 = decisionTemplate4.format(a = name)

        if len(data_line) > 1:
            state = data_line[0]
            decisionStr1 += decisionTemplate1.format(a = state)
            decisionStr3 += decisionTemplate3.format(a = state)
            decisionStr5 += decisionTemplate5.format(a = state)

    print(rewrite_data)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(rewrite_data)