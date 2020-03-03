
import json

def party_xp_threshold(party_size):
    '''Function that takes party size and levels of players, and adds their
    xp thresholds to return a list which can be used for random encounters'''

    #Load xp threshold dictionary to use
    xp_dict = 'xp_threshold_dict.txt'
    with open(xp_dict) as json_file:
        xp_thresholds = json.load(json_file)

    #party_size is an integer, pc_level should become a list to run through
    #create list with user input
    pc_level_list = []
    pc_count = 0
    for pc in range(1, (party_size + 1)):
        pc_count += 1
        str_pc = str(pc_count)
        level = int(input('Input level of player'+str_pc+': '))
        pc_level_list.append(level)

    # create empty list that has a zero for each threshold
    final_xp_thresholds = [0,0,0,0]

    #run for loop for each element in pc_level_list
    for pc_level in pc_level_list:
        for key, threshold in xp_thresholds.items():
            if int(key) == pc_level:
                for i in range (0,4):
                    final_xp_thresholds[i] += threshold[i]

    return final_xp_thresholds


