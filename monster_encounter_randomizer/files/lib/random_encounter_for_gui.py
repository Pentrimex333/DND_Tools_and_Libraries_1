# Function that produces a group of monsters that a party can fight
import json
from random import choice, randint
from lib import monster_search as monsters
from lib import mon_xp_modifier as xp_mod


def encounter(party_size, xp_threshold, mon_type, min_xp=0,
              max_xp=160000, location=''): 
#'''Takes a party's xp thresholds, selects threshold based on difficulty
#chosen, then chooses a random group of monsters of certain criteria
#whose XP value sum up to or just below that threshold.'''

    # Determine party xp threshold, then choose threshold based on difficulty
    chosen_threshold = xp_threshold
    print("chosen threshold for party is:",chosen_threshold)
    print(type(chosen_threshold))
    print("Party Size:", party_size)
    print("Monster Types:", mon_type)
    print("minimum xp:", min_xp)
    print('max xp:', max_xp)
    print("Location:", location)
    ### Get monsters that fit desired criteria, and get count of monsters
    eligible_monsters = monsters.search(mon_type, min_xp, max_xp, location)
    monster_count = len(eligible_monsters)

    
    ### Create a while loop that randomly chooses monsters from
    ### eligible_monsters and adds them to encounter_group, until
    ### they are within 10% of the range of the threshold given.

    ### May need to add an if statement that checks whether any of the
    ###monsters in eligible_monsters can still fit the criteria, and then
    ###breaks if there is not.
    encounter_group = {}
    adjusted_mon_xp = 0
    unadjusted_mon_xp = 0
    xp_remaining = chosen_threshold
    unfilled = True
    while unfilled == True:
        rand_monster = monster, stats = choice(list(eligible_monsters.items()))
        if rand_monster[0] in encounter_group.keys(): #Duplicates mess up XP count
            print('Monster already in encounter, moving on!')
            continue
        print(rand_monster)
        xp_finder = rand_monster[1]
        current_mon_xp = xp_finder['XP']
        unadjusted_mon_xp += current_mon_xp

    #Below are the if statements to include xp modifiers based on party_size
    #and number of monsters in current encounter group.
        adjusted_mon_xp = xp_mod.xp_adjustment(unadjusted_mon_xp, encounter_group,
                                        party_size)

        xp_remaining = chosen_threshold - adjusted_mon_xp
        
        if adjusted_mon_xp <= chosen_threshold:
            encounter_group[rand_monster[0]] = rand_monster[1]
            if current_mon_xp <= (chosen_threshold * 0.1) and current_mon_xp <=450:
                rand_num = randint(2,8)
                for i in range(1,rand_num):
                    x = str(i+1)
                    multiple_mon_name = rand_monster[0]+" "+x
                    unadjusted_mon_xp += current_mon_xp
                    adjusted_mon_xp = xp_mod.xp_adjustment(unadjusted_mon_xp,
                                                    encounter_group,
                                                    party_size=party_size)
                    if adjusted_mon_xp <= chosen_threshold:
                        encounter_group[multiple_mon_name] = rand_monster[1]
                        print('# of Monsters:', len(encounter_group))
                        print('Without Adjustment XP:',unadjusted_mon_xp)
                        print("Adjusted XP Value:", adjusted_mon_xp)
                    else:
                        unadjusted_mon_xp -=current_mon_xp
                        adjusted_mon_xp = xp_mod.xp_adjustment(unadjusted_mon_xp,
                                                        encounter_group, party_size)
                        print('Too High: Monster XP being removed')
                        print('Without Adjustment XP for removal:',unadjusted_mon_xp)
                        print('Adjusted XP Value:', adjusted_mon_xp)
                        break
            else:
                pass
            print("current encounter group is:",encounter_group)
        else:
            pass
        # This check clears and restarts list if it accidentally goes over
        # chosen_threshold
        if adjusted_mon_xp > chosen_threshold:
            encounter_group = {}
            adjusted_mon_xp = 0
            unadjusted_mon_xp = 0
            print("EXCEEDED XP THRESHOLD; RESTARTING ENCOUNTER GROUP!")
        elif adjusted_mon_xp >= (chosen_threshold * 0.67):
            unfilled = False
            final_encounter_group = sorted(encounter_group.items())
            print('Here is your monster list:\n',sorted(encounter_group.keys()))
            print('XP Value of this encounter =',adjusted_mon_xp)

    return [final_encounter_group, adjusted_mon_xp]
        #run a check as to whether any monsters in eligible_monsters
        #can still fall within the acceptable XP range remaining.