#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def create_monster(new_monster_name): #new_monster_name must be string values
    
    #first, we need to import the txt file holding monster_list_1
    import json

    with open('monster_list_1.txt') as json_file:
        monster_list_1 = json.load(json_file)

    for key in monster_list_1.keys():   #Checks that monster already exists
        if key == new_monster_name:
            print('Monster already included in List')
            return   #If monster already exists, quit current iteration

    new_monster_dict = {}    #Dictionary to become value for new_monster_name
    
    #inputs for dictionary including creature stats
    creature_type = input('What is the creature type? ')
    hp = int(input('What is the HP of the creature? '))
    armor = int(input('What is the AC of the creature? '))
    speed = input('What is the speed of the creature? ')
    xp = int(input('How much XP is the creature worth? '))
    terrain = input('What terrain does this creature prefer? ' )
    book = input('Where is the info for this creature located? ')
    
    #stats for new_monster_name compiled into a dictionary
    new_monster_dict['Type'] = creature_type.title()
    new_monster_dict['HP'] = hp
    new_monster_dict['AC'] = armor 
    new_monster_dict['Speed'] = speed.title()
    new_monster_dict['XP'] = xp 
    new_monster_dict['Located'] = terrain.title()
    new_monster_dict['Book'] = book.upper()


    final_check = input('\nAre you sure all of the info is correct? (Y/N): ')
    if final_check.upper() == 'Y':
        monster_list_1[new_monster_name] = new_monster_dict # Makes dictionary entry
    else:
        pass
# with new_monster_name as the key and new_monster_dict as the value.


    
    #now we need to convert monster_list_1 back into a txt file
    with open('monster_list_1.txt', 'w') as temp_list:
        json.dump(monster_list_1, temp_list, sort_keys=True, indent=4)


def main():

    while True:
        new_monster_name = input('\nInsert Monster name: ').title()
        create_monster(new_monster_name)
        check = input('Do you want to add another monster (Y/N): ').upper()
        if check == 'N':
            break


main()
