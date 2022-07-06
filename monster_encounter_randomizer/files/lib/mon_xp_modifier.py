def xp_adjustment(unadjusted_mon_xp, encounter_group, party_size):
    '''For taking the unadjusted xp of a monster, and modifying it so that
       the total xp of an encounter accounts for party size and number of
       monsters.'''
    if(len(encounter_group)+1) == 1 and party_size>=6:
        adjusted_mon_xp = round(unadjusted_mon_xp * 0.5)
    elif(len(encounter_group)+1) == 1 and party_size in (3,4,5):
        adjusted_mon_xp = unadjusted_mon_xp
    elif(len(encounter_group)+1) == 1 and party_size in (1,2):
        adjusted_mon_xp = round(unadjusted_mon_xp * 0.5)
    elif(len(encounter_group)+1) == 2 and party_size>=6:
        adjusted_mon_xp = unadjusted_mon_xp
    elif(len(encounter_group)+1) == 2 and party_size in (3,4,5):
        adjusted_mon_xp = round(unadjusted_mon_xp * 1.5)
    elif(len(encounter_group)+1) == 2 and party_size in (1,2):
        adjusted_mon_xp = round(unadjusted_mon_xp * 2)
    elif(len(encounter_group)+1) in (3,4,5,6) and party_size>=6:
        adjusted_mon_xp = round(unadjusted_mon_xp * 1.5)
    elif(len(encounter_group)+1) in (3,4,5,6) and party_size in (3,4,5):
        adjusted_mon_xp = round(unadjusted_mon_xp * 2)
    elif(len(encounter_group)+1) in (3,4,5,6) and party_size in (1,2):
        adjusted_mon_xp = round(unadjusted_mon_xp * 2.5)
    elif(len(encounter_group)+1) in (7,8,9,10) and party_size>=6:
        adjusted_mon_xp = round(unadjusted_mon_xp * 2)
    elif(len(encounter_group)+1) in (7,8,9,10) and party_size in (3,4,5):
        adjusted_mon_xp = round(unadjusted_mon_xp * 2.5)
    elif(len(encounter_group)+1) in (7,8,9,10) and party_size in (1,2):
        adjusted_mon_xp = round(unadjusted_mon_xp * 3)
    elif(len(encounter_group)+1) in (11,12,13,14) and party_size>=6:
        adjusted_mon_xp = round(unadjusted_mon_xp * 2.5)
    elif(len(encounter_group)+1) in (11,12,13,14) and party_size in (3,4,5):
        adjusted_mon_xp = round(unadjusted_mon_xp * 3)
    elif(len(encounter_group)+1) in (11,12,13,14) and party_size in (1,2):
        adjusted_mon_xp = round(unadjusted_mon_xp * 4)
    elif(len(encounter_group)+1) >= 15 and party_size>=6:
        adjusted_mon_xp = round(unadjusted_mon_xp * 3)
    elif(len(encounter_group)+1) >= 15 and party_size in (3,4,5):
        adjusted_mon_xp = round(unadjusted_mon_xp * 4)
    elif(len(encounter_group)+1) >= 15 and party_size in (1,2):
            adjusted_mon_xp = round(unadjusted_mon_xp * 5)

    return adjusted_mon_xp
