# This function searches through the master_monster_list to identify
# any monsters that meet all given criteria.
import json
import os

def search(mon_type, min_xp=0, max_xp=160000, location=''):
    '''Function that sequentially checks if a monster meets all requirements,
    then adds them to a returned dictionary for further use in later modules'''

    #First, use json to open the monster_list
    cwd = os.getcwd()
    current_monster_list = "\\lib\\master_monster_list.txt"
    with open(cwd + current_monster_list) as json_file:
        monster_database = json.load(json_file)

    #Set a new dictionary to hold searched monsters
    prelim_chosen_monsters = {}
    chosen_monsters = {}   
     
    #Create a for loop that searches through monsters in monster_list 
    for monster, stats in monster_database.items():
        
        # Sequential if statements which weed out based on type, then XP range, and finally location
        for monster_type in mon_type:
            if monster_type in stats['Type']:
                prelim_chosen_monsters[monster] = stats

    for monster, stats in prelim_chosen_monsters.items():
        if stats['XP'] >= min_xp and stats['XP'] <= max_xp:
            if location in stats['Located']:
                    
            #if all criteria are met, then monster is added to chosen_monsters
                chosen_monsters[monster] = stats
        
        #TYPE = stats.get('Type')
        
        #print(TYPE)
        #if monster_type in TYPE:
            #print('FOUND:',monster_type)
        
    return chosen_monsters
                    
def test():
    stuff = search(mon_type='Fiend',location='Planar')
    print("LENGHT:",len(stuff))
    print(stuff)
#test()
# In[ ]:




