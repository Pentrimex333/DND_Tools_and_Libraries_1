#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

def search(mon_type='', min_xp=0, max_xp=160000, location=''):
    '''Function that sequentially checks if a monster meets all requirements,
    then adds them to a returned dictionary for further use in later modules'''    
    
    #First, use json to open the monster_list
    current_monster_list = 'monster_list_test.txt'
    with open(current_monster_list) as json_file:
        monster_database = json.load(json_file)
        
    #Set a new dictionary to hold searched monsters
    chosen_monsters = {}    
    
    #Create a for loop that searches through monsters in monster_list 
    for monster, stats in monster_database.items():
        
        # Sequential if statements which weed out based on type, then XP range, and finally location
        if mon_type.title() in stats['Type']:
            if stats['XP'] >= min_xp and stats['XP'] <= max_xp:
                if location.title() in stats['Located']:
                    
                    #if all criteria are met, then monster is added to chosen_monsters
                    chosen_monsters[monster] = stats
    
    return chosen_monsters
                    


# In[ ]:




