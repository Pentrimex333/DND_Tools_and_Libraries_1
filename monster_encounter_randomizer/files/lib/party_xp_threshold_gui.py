#This function calculates the XP Threshold for a party, with levels for each
#party member given in a list format.
import json
import os

def party_xp_threshold(pc_level_list):
    '''Function that takes party size and levels of players, and adds their
    xp thresholds to return a list which can be used for random encounters'''

    #Load xp threshold dictionary to use
    cwd = os.getcwd()
    xp_dict = '\\lib\\xp_threshold_dict.txt'
    with open(cwd + xp_dict) as json_file:
        xp_thresholds = json.load(json_file)
        print(xp_thresholds)

    #party_size is an integer, pc_level should become a list to run through
    #create list with user input
    #global pc_level_list
    #print(pc_level_list)

    # create empty list that has a zero for each threshold
    final_xp_thresholds = [0,0,0,0]

    #run for loop for each element in pc_level_list
    for pc_level in pc_level_list:
        for key, threshold in xp_thresholds.items():
            if int(key) == pc_level:
                for i in range (0,4):
                    final_xp_thresholds[i] += threshold[i]

    return final_xp_thresholds


