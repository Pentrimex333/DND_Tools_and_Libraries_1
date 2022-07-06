from lib import random_encounter_for_gui as rand_enc
from lib import party_xp_threshold_gui as party_xp
from tkinter import *

pc_level_list = []
num_of_players = 0
xp_thresholds = []

# Include lib folder in the current path
#sys.path.insert(1, '\\lib')

#################
### FUNCTIONS ###
#################
    
def submit_level():
    '''On button push, takes integer in entry box and adds it to pc_level_list, then
    clears it in preparation for next level entry while displaying current list.'''
    global pc_level_list
    x = int(pc_level_entry.get())
    pc_level_entry.delete(0, END)
    pc_level_list.append(x)
    pc_level_list_tracker.config(text=str(pc_level_list))

def xp_display():
    '''On button push, runs party_xp_threshold function, then stores xp thresholds
    into xp_thresholds list and displays difficulty values to user.'''
    global pc_level_list
    global xp_thresholds
    global num_of_players
    num_of_players = len(pc_level_list)
    print(num_of_players)
    xp_thresholds = party_xp.party_xp_threshold(pc_level_list)
    xp_intro_label.grid(row=6, column=0, columnspan=2)
    xp_easy_label.grid(row=7, column=0, sticky=E)
    xp_easy_value = Label(xp_frame, text=str(xp_thresholds[0]), bg='gray70',
                          font='Verdana 8 bold')
    xp_easy_value.grid(row=7, column=1, sticky=W)
    xp_medium_label.grid(row=8, column=0, sticky=E)
    xp_medium_value = Label(xp_frame, text=str(xp_thresholds[1]), bg='gray70',
                            font='Verdana 8 bold')
    xp_medium_value.grid(row=8, column=1, sticky=W)
    xp_hard_label.grid(row=9, column=0, sticky=E)
    xp_hard_value = Label(xp_frame, text=str(xp_thresholds[2]), bg='gray70',
                          font='Verdana 8 bold')
    xp_hard_value.grid(row=9, column=1, sticky=W)
    xp_deadly_label.grid(row=10, column=0, sticky=E)
    xp_deadly_value = Label(xp_frame, text=str(xp_thresholds[3]), bg='gray70',
                            font='Verdana 8 bold')
    xp_deadly_value.grid(row=10, column=1, sticky=W)
    pc_level_list = []

def encounter_display():
    '''On button push, collect all necessary info including desired xp threshold,
    monster types, and chosen terrain, and then compile these into local
    variables that can be inserted into imported encounter function. Finally,
    display this information in a manner that is easily readable.'''
    global xp_thresholds
    global chosen_difficulty
    global chosen_terrain
    global num_of_players
    global enc_group_frame
    global aberration_choice, beast_choice, celestial_choice, construct_choice
    global dragon_choice, elemental_choice, fey_choice, giant_choice
    global lycanthrope_choice, monstrosity_choice, ooze_choice, plant_choice
    global undead_choice, yuanti_choice, anyfiend_choice, demon_choice
    global devil_choice, yugoloth_choice, anyhuman_choice, bullywug_choice
    global derro_choice, drow_choice, duergar_choice, firenewt_choice
    global giff_choice, gith_choice, gnoll_choice, goblin_choice, grung_choice
    global kobold_choice, kuotoa_choice, lizardfolk_choice, meazel_choice
    global orc_choice, sahuagin_choice, shadarkai_choice, thrikreen_choice
    global troglodyte_choice, xvart_choice
    
    
    #1) Set xp threshold value based on chosen radio button
    if chosen_difficulty.get() == 1:
        chosen_threshold = xp_thresholds[0]
    elif chosen_difficulty.get() == 2:
        chosen_threshold = xp_thresholds[1]
    elif chosen_difficulty.get() == 3:
        chosen_threshold = xp_thresholds[2]
    elif chosen_difficulty.get() == 4:
        chosen_threshold = xp_thresholds[3]
    else:
        difficulty_error = Label(main_window, text='Please select difficulty')
        difficulty_error.grid(row=5, column=5) # Set underneath encounter button
        return
    print("Chosen threshold value is:",chosen_threshold) #To check that this works
    
    #2) Set terrain value based on chosen radio button (This is already chosen
    #due to setting string variable chosen_terrain to terrain value
    encounter_terrain = ''
    if chosen_terrain.get() == "None":
        encounter_terrain = ''    # If None is selected, then empty value for function
    else:
        encounter_terrain = chosen_terrain.get()
    print("Chosen Terrain is:", encounter_terrain)
    
    #3) Compile monster types to be chosen using a string addition format
    chosen_montypes = (aberration_choice.get()+beast_choice.get()+
                       celestial_choice.get()+construct_choice.get()+
                       dragon_choice.get()+elemental_choice.get()+
                       fey_choice.get()+giant_choice.get()+
                       lycanthrope_choice.get()+monstrosity_choice.get()+
                       ooze_choice.get()+plant_choice.get()+undead_choice.get()+
                       yuanti_choice.get()+anyfiend_choice.get()+
                       demon_choice.get()+devil_choice.get()+
                       yugoloth_choice.get()+anyhuman_choice.get()+
                       bullywug_choice.get()+derro_choice.get()+
                       drow_choice.get()+duergar_choice.get()+
                       firenewt_choice.get()+giff_choice.get()+
                       gith_choice.get()+gnoll_choice.get()+goblin_choice.get()+
                       grung_choice.get()+kobold_choice.get()+
                       kuotoa_choice.get()+lizardfolk_choice.get()+
                       meazel_choice.get()+orc_choice.get()+
                       sahuagin_choice.get()+shadarkai_choice.get()+
                       thrikreen_choice.get()+
                       troglodyte_choice.get()+xvart_choice.get())
    split_types = chosen_montypes.rstrip(' ')
    chosen_montypes = split_types.split(' ')
    print("Chosen monster types include:",chosen_montypes) # Check

    ### CREATE A SECTION ALSO FOR TAKING IN XP RANGE OF MONSTERS (FIRST CREATE
    ### GUI SECTION TO INPUT THIS INFO, THEN ADD IT HERE AND FINALLY CREATE
    ### AN IF CHECK THAT STOPS THE FUNCTION IF XP RANGE EXCEEDS THRESHOLD.
    MIN_XP = int(min_xp_entry.get())
    MAX_XP = int(max_xp_entry.get())
    
    #4) Take local variables for three options above, and set them into the
    #imported encounter function
    encounter_output = rand_enc.encounter(party_size=num_of_players,
                                 xp_threshold=chosen_threshold,
                                 mon_type=chosen_montypes, min_xp=MIN_XP,
                                 max_xp=MAX_XP, location=encounter_terrain)
    encounter_group_tuples = encounter_output[0]
    encounter_group_xp_value = encounter_output[1]
    
    #5) Display the chosen monsters into either a popup window or a lower
    #spot in the grid of main_window and structure this output to put all
    #important stats in a row next to monster names.
    enc_group_frame.destroy()
    enc_group_frame = LabelFrame(main_window, text="Your Encounter Group",
                                 labelanchor='n', padx=5, pady=5, bd=15, 
                                 font='Verdana 11 bold underline', relief=RIDGE,)                                 
    enc_group_frame.grid(row=1, column=2, rowspan=4, sticky=N)

    name_label = Label(enc_group_frame, text="Monster Name",
                       font='Verdana 9 bold underline', padx=10, pady=5)
    name_label.grid(row=0, column=0, sticky=W)
    hp_label = Label(enc_group_frame, text="HP Total",
                     font='Verdana 9 bold underline', padx=10, pady=5)
    hp_label.grid(row=0, column=1)
    ac_label = Label(enc_group_frame, text="AC", font='Verdana 9 bold underline',
                     padx=10, pady=5)
    ac_label.grid(row=0, column=2)
    speed_label = Label(enc_group_frame, text="Speed",
                        font='Verdana 9 bold underline', padx=10, pady=5)
    speed_label.grid(row=0, column=3)
    book_label = Label(enc_group_frame, text="Book / Page",
                       font='Verdana 9 bold underline', padx=10, pady=5)
    book_label.grid(row=0, column=4)
                             
    for num, monster in enumerate(encounter_group_tuples):
        print(num)
        print(type(num))
        mon_name = monster[0]
        mon_label = Label(enc_group_frame, text=mon_name, padx=5, fg='red')
        mon_label.configure(font='Verdana 8 bold', bd=3, relief=GROOVE)
        mon_label.grid(row=num+1, column=0)

        stats = monster[1]
        stats_list = list(stats.values())
        
        ac_value = stats_list[0]
        mon_ac_label = Label(enc_group_frame, text=str(ac_value), padx=5)
        mon_ac_label.grid(row=num+1, column=2)

        book_value = stats_list[1]
        mon_book_label = Label(enc_group_frame, text=book_value, padx=5)
        mon_book_label.grid(row=num+1, column=4)

        hp_value = stats_list[2]
        mon_hp_label = Label(enc_group_frame, text=str(hp_value), padx=5)
        mon_hp_label.grid(row=num+1, column=1)

        speed_value = stats_list[4]
        mon_speed_label = Label(enc_group_frame, text=speed_value, padx=5)
        mon_speed_label.grid(row=num+1, column=3)

    encounter_xp_label = Label(enc_group_frame, text='Encounter Total XP:',
                               padx=5, pady=10, font='Verdana 10 bold')
    encounter_xp_label.grid(row=99, column=0, columnspan=2, sticky=S)
    encounter_xp_value = Label(enc_group_frame, padx=5, pady=10,
                               text=str(encounter_group_xp_value),
                               font='Verdana 10 bold')
    encounter_xp_value.grid(row=99, column=2, sticky=S)

                             
###############################################################################    

main_window = Tk()
main_window.title("Random Encounter Generator v2.2")

#############################
### XP THRESHOLDS SECTION ###
#############################
xp_frame = LabelFrame(main_window, bd=18, bg='gray70', text=' XP Thresholds ',
                      font='Verdana 11 underline bold', relief=RIDGE, padx=5,
                      pady=5, labelanchor='n', height=500)
xp_frame.grid(row=0, column=0, rowspan=2, sticky='N')
pc_level_intro = Label(xp_frame, text=
                       '''Enter the level for each player, and then hit the 'SUBMIT LV' button.
Hit 'FINISHED' when all levels have been entered.''', bg='gray70', fg='white')
pc_level_intro.configure(font='Verdana 8 bold')
pc_level_intro.grid(row=1, column=0, columnspan=2, pady=2)
pc_level_entry = Entry(xp_frame, width=4)
pc_level_entry.grid(row=2, column=1, sticky=W)
pc_level_label = Label(xp_frame, text="Enter Player Level:", bg='gray70',
                       font='Verdana 8 bold', fg='firebrick1')
pc_level_label.grid(row=2, column=0, sticky=E)
pc_level_submit_button = Button(xp_frame, text="SUBMIT LV", font='Arial 9 bold',
                                command=submit_level, bg='gold')
pc_level_submit_button.grid(row=3, column=1, pady=5)
pc_level_complete_button = Button(xp_frame, text="FINISHED", bg='green3',
                                  command=xp_display, font='Arial 9 bold')
pc_level_complete_button.grid(row=4, column=1)

pc_level_list_tracker = Label(xp_frame, text=str(pc_level_list), anchor='w',
                              bg='gray70')
pc_level_list_tracker.grid(row=4, column=0)
pc_level_list_label = Label(xp_frame, text='''Inputted player levels
shown below:''',
                            bg='gray70')
pc_level_list_label.grid(row=3, column=0)

xp_intro_label = Label(xp_frame,
                       text='''Here are the XP thresholds for your party!''',
                       bg='gray70', pady=5, font = 'Verdana 10 bold')
xp_easy_label = Label(xp_frame, text='Easy =', bg='gray70')
xp_medium_label = Label(xp_frame, text='Medium =', bg='gray70')
xp_hard_label = Label(xp_frame, text='Hard =', bg='gray70')
xp_deadly_label = Label(xp_frame, text='Deadly =', bg='gray70')

################################################################################

################################
### MONSTER XP RANGE SECTION ###
################################

mon_xp_range_frame = LabelFrame(main_window, bd=20, bg='gray70',
                                text='''Monster XP
Range''', labelanchor='n', 
                                font='Verdana 10 underline bold', relief=RIDGE,
                                pady=5, padx=5)
mon_xp_range_frame.grid(row=1, column=1)

min_xp_range_label = Label(mon_xp_range_frame, text='Min XP Value:',
                           bg='gray70')
min_xp_range_label.grid(row=1, column=0, sticky=E)
min_xp_entry = Entry(mon_xp_range_frame, width=7)
min_xp_entry.insert(0, '0')
min_xp_entry.grid(row=1, column=1, sticky=W)

max_xp_range_label = Label(mon_xp_range_frame, text='Max XP Value:',
                           bg='gray70', pady=5)
max_xp_range_label.grid(row=2, column=0, sticky=E)
max_xp_entry = Entry(mon_xp_range_frame, width=7)
max_xp_entry.insert(0, '155000')
max_xp_entry.grid(row=2, column=1, sticky=W)

################################################################################

#################################################################
### MONSTER TYPE, CR LIMITS, AND DIFFICULTY SELECTION SECTION ###
#################################################################

### DIFFICULTY SECTION ###

chosen_difficulty = IntVar()
chosen_difficulty.set(1)

difficulty_frame = LabelFrame(main_window, bd=15, bg='gray70', pady=15,
                              padx=30, labelanchor='n',
                              relief=RIDGE, text=" Difficulty ", 
                              font='Verdana 12 underline bold')
difficulty_frame.grid(row=0, column=1)

easy_choice = Radiobutton(difficulty_frame, text="Easy", bg='lawn green',
                          variable=chosen_difficulty, value=1)
easy_choice.configure(font='Verdana 10 bold')
easy_choice.grid(row=1, column=0)
medium_choice = Radiobutton(difficulty_frame, text="Medium", bg='yellow2',
                            variable=chosen_difficulty, value=2)
medium_choice.configure(font='Verdana 10 bold')
medium_choice.grid(row=2, column=0)
hard_choice = Radiobutton(difficulty_frame, text="Hard", bg='coral1',
                          variable=chosen_difficulty, value=3)
hard_choice.configure(font='Verdana 10 bold')
hard_choice.grid(row=3, column=0)
deadly_choice = Radiobutton(difficulty_frame, text="Deadly", bg='firebrick2',
                            variable=chosen_difficulty, value=4)
deadly_choice.configure(font='Verdana 10 bold')
deadly_choice.grid(row=4, column=0)

########################################

### TERRAIN SECTION ###

chosen_terrain = StringVar()
chosen_terrain.set("None")

terrain_frame = LabelFrame(main_window, text=" Terrain Options ", bd=15,
                           relief=RIDGE, font='Verdana 11 underline bold',
                           pady=5, padx=10, labelanchor='n', bg='gray80')
terrain_frame.grid(row=2, column=0)

arctic_choice = Radiobutton(terrain_frame, text="Arctic", bg='gray80',
                            variable=chosen_terrain, value="Arctic",
                            font='Verdana 9')
arctic_choice.grid(row=0, column=0, padx=35)
cemetery_choice = Radiobutton(terrain_frame, text="Cemetery", bg='gray80',
                              variable=chosen_terrain, value="Cemetery",
                              font='Verdana 9')
cemetery_choice.grid(row=1, column=0)
coast_choice = Radiobutton(terrain_frame, text="Coast", bg='gray80',
                           variable=chosen_terrain, value="Coast",
                           font='Verdana 9')
coast_choice.grid(row=2, column=0)
desert_choice = Radiobutton(terrain_frame, text="Desert", bg='gray80',
                            variable=chosen_terrain, value="Desert",
                            font='Verdana 9')
desert_choice.grid(row=3, column=0)
forest_choice = Radiobutton(terrain_frame, text="Forest", bg='gray80',
                            variable=chosen_terrain, value="Forest",
                            font='Verdana 9')
forest_choice.grid(row=4, column=0)
grassland_choice = Radiobutton(terrain_frame, text="Grassland", bg='gray80',
                               variable=chosen_terrain, value="Grassland",
                               font='Verdana 9')
grassland_choice.grid(row=0, column=1, padx=35)
hill_choice = Radiobutton(terrain_frame, text="Hill", bg='gray80',
                          variable=chosen_terrain, value="Hill",
                          font='Verdana 9')
hill_choice.grid(row=1, column=1)
jungle_choice = Radiobutton(terrain_frame, text="Jungle", bg='gray80',
                            variable=chosen_terrain, value="Jungle",
                            font='Verdana 9')
jungle_choice.grid(row=2, column=1)
mountain_choice = Radiobutton(terrain_frame, text="Mountain", bg='gray80',
                              variable=chosen_terrain, value="Mountain",
                              font='Verdana 9')
mountain_choice.grid(row=3, column=1)
planar_choice = Radiobutton(terrain_frame, text="Planar", bg='gray80',
                            variable=chosen_terrain, value="Planar",
                            font='Verdana 9')
planar_choice.grid(row=4, column=1)
swamp_choice = Radiobutton(terrain_frame, text="Swamp", bg='gray80',
                           variable=chosen_terrain, value="Swamp",
                           font='Verdana 9')
swamp_choice.grid(row=0, column=2, padx=35)
underdark_choice = Radiobutton(terrain_frame, text="Underdark", bg='gray80',
                               variable=chosen_terrain, value="Underdark",
                               font='Verdana 9')
underdark_choice.grid(row=1, column=2)
underwater_choice = Radiobutton(terrain_frame, text="Underwater", bg='gray80',
                                variable=chosen_terrain, value="Underwater",
                                font='Verdana 9')
underwater_choice.grid(row=2, column=2)
urban_choice = Radiobutton(terrain_frame, text="Urban", bg='gray80',
                           variable=chosen_terrain, value="Urban",
                           font='Verdana 9')
urban_choice.grid(row=3, column=2)

no_terrain_choice = Radiobutton(terrain_frame, text="None", bg='gray80',
                                variable=chosen_terrain, value="None",
                                font='Verdana 9')
no_terrain_choice.grid(row=4, column=2)

#####################################

### CREATURE TYPE SECTION ###

creaturetype_frame = LabelFrame(main_window, text=" Choose Creature Type(s) ",
                                padx=5, pady=10, bd=15, relief=RIDGE,
                                bg='gray80', font='Verdana 11 underline bold',
                                labelanchor='n')
creaturetype_frame.grid(row=3, column=0, columnspan=2)
# ABERRATIONS #
aberration_choice = StringVar()
aberration_check = Checkbutton(creaturetype_frame, text="Aberration",
                               variable=aberration_choice,
                               onvalue="Aberration ", offvalue="", bg='gray80')
aberration_check.grid(row=0, column=0)
# BEASTS #
beast_choice = StringVar()
beast_check = Checkbutton(creaturetype_frame, text="Beast",
                               variable=beast_choice, onvalue="Beast ",
                               offvalue="", bg='gray80')
beast_check.grid(row=1, column=0)
# CELESTIALS #
celestial_choice = StringVar()
celestial_check = Checkbutton(creaturetype_frame, text="Celestial",
                              variable=celestial_choice,
                              onvalue="Celestial ", offvalue="", bg='gray80')
celestial_check.grid(row=2, column=0)
# CONSTRUCTS #
construct_choice = StringVar()
construct_check = Checkbutton(creaturetype_frame, text="Construct",
                              variable=construct_choice,
                              onvalue="Construct ", offvalue="", bg='gray80')
construct_check.grid(row=3, column=0)
# DRAGONS #
dragon_choice = StringVar()
dragon_check = Checkbutton(creaturetype_frame, text="Dragon",
                           variable=dragon_choice, onvalue="Dragon ",
                           offvalue="", bg='gray80')
dragon_check.grid(row=4, column=0)
# ELEMENTALS #
elemental_choice = StringVar()
elemental_check = Checkbutton(creaturetype_frame, text="Elemental",
                              variable=elemental_choice,
                              onvalue="Elemental ", offvalue="", bg='gray80')
elemental_check.grid(row=5, column=0)
# FEY #
fey_choice = StringVar()
fey_check = Checkbutton(creaturetype_frame, text="Fey",
                        variable=fey_choice, onvalue="Fey ",
                        offvalue="", bg='gray80')
fey_check.grid(row=6, column=0)
# GIANTS #
giant_choice = StringVar()
giant_check = Checkbutton(creaturetype_frame, text="Giant",
                          variable=giant_choice, onvalue="Giant ",
                          offvalue="", bg='gray80')
giant_check.grid(row=0, column=1)
# LYCANTHROPES #
lycanthrope_choice = StringVar()
lycanthrope_check = Checkbutton(creaturetype_frame, text="Lycanthrope",
                                variable=lycanthrope_choice, bg='gray80',
                                onvalue="Lycanthrope ", offvalue="")
lycanthrope_check.grid(row=1, column=1)
# MONSTROSITIES #
monstrosity_choice = StringVar()
monstrosity_check = Checkbutton(creaturetype_frame, text="Monstrosity",
                                variable=monstrosity_choice, bg='gray80',
                                onvalue="Monstrosity ", offvalue="")
monstrosity_check.grid(row=2, column=1)
# OOZES #
ooze_choice = StringVar()
ooze_check = Checkbutton(creaturetype_frame, text="Ooze",
                         variable=ooze_choice, onvalue="Ooze ",
                         offvalue="", bg='gray80')
ooze_check.grid(row=3, column=1)
# PLANTS #
plant_choice = StringVar()
plant_check = Checkbutton(creaturetype_frame, text="Plant",
                          variable=plant_choice, onvalue="Plant ",
                          offvalue="", bg='gray80')
plant_check.grid(row=4, column=1)
# UNDEAD #
undead_choice = StringVar()
undead_check = Checkbutton(creaturetype_frame, text="Undead",
                           variable=undead_choice, onvalue="Undead ",
                           offvalue="", bg='gray80')
undead_check.grid(row=5, column=1)
# YUAN-TI #
yuanti_choice = StringVar()
yuanti_check = Checkbutton(creaturetype_frame, text="Yuan-Ti",
                           variable=yuanti_choice, onvalue="Yuan-Ti ",
                           offvalue="", bg='gray80')
yuanti_check.grid(row=6, column=1)

# The fiend creature type options below are framed individually for multiple options
fiend_section = LabelFrame(creaturetype_frame, text="FIENDS", padx=5, pady=5,
                           bd=5, bg='gray80', font='Verdana 9 bold',
                           labelanchor='n')
fiend_section.grid(row=0, column=2, rowspan=5, padx=45)
# ALL FIENDS #
anyfiend_choice = StringVar()
anyfiend_check = Checkbutton(fiend_section, text="Any",
                             variable=anyfiend_choice, onvalue="Fiend ",
                             offvalue="", bg='gray80')
anyfiend_check.grid(row=0, column=0)
# DEMONS #
demon_choice = StringVar()
demon_check = Checkbutton(fiend_section, text="Demon",
                          variable=demon_choice, onvalue="Demon ",
                          offvalue="", bg='gray80')
demon_check.grid(row=1, column=0)
# DEVILS #
devil_choice = StringVar()
devil_check = Checkbutton(fiend_section, text="Devil",
                          variable=devil_choice, onvalue="Devil ",
                          offvalue="", bg='gray80')
devil_check.grid(row=2, column=0)
# YUGOLOTHS #
yugoloth_choice = StringVar()
yugoloth_check = Checkbutton(fiend_section, text="Yugoloth",
                             variable=yugoloth_choice, onvalue="Yugoloth ",
                             offvalue="", bg='gray80')
yugoloth_check.grid(row=3, column=0)

#Humanoid creature type options also framed individually below
human_section = LabelFrame(creaturetype_frame, text="HUMANOIDS",
                           padx=5, pady=5, bg='gray80', bd=5, labelanchor='n',
                           font='Verdana 9 bold')
human_section.grid(row=0, column=3, columnspan=3, rowspan=7)
# ALL HUMANOIDS #
anyhuman_choice = StringVar()
anyhuman_check = Checkbutton(human_section, text="Any",
                             variable=anyhuman_choice, onvalue="Humanoid ",
                             offvalue="", bg='gray80')
anyhuman_check.grid(row=0, column=0)
# BULLYWUGS #
bullywug_choice = StringVar()
bullywug_check = Checkbutton(human_section, text="Bullywug",
                             variable=bullywug_choice, onvalue="Bullywug ",
                             offvalue="", bg='gray80')
bullywug_check.grid(row=1, column=0)
# DERRO #
derro_choice = StringVar()
derro_check = Checkbutton(human_section, text="Derro",
                          variable=derro_choice, onvalue="Derro ",
                          offvalue="", bg='gray80')
derro_check.grid(row=2, column=0)
# DROW #
drow_choice = StringVar()
drow_check = Checkbutton(human_section, text="Drow",
                         variable=drow_choice, onvalue="Drow ",
                         offvalue="", bg='gray80')
drow_check.grid(row=3, column=0)
# DUERGAR #
duergar_choice = StringVar()
duergar_check = Checkbutton(human_section, text="Duergar",
                            variable=duergar_choice, onvalue="Duergar ",
                            offvalue="", bg='gray80')
duergar_check.grid(row=4, column=0)
# FIRENEWTS #
firenewt_choice = StringVar()
firenewt_check = Checkbutton(human_section, text="Firenewt",
                             variable=firenewt_choice, onvalue="Firenewt ",
                             offvalue="", bg='gray80')
firenewt_check.grid(row=5, column=0)
# GIFF #
giff_choice = StringVar()
giff_check = Checkbutton(human_section, text="Giff",
                         variable=giff_choice, onvalue="Giff ",
                         offvalue="", bg='gray80')
giff_check.grid(row=6, column=0)
# GITH #
gith_choice = StringVar()
gith_check = Checkbutton(human_section, text="Gith",
                         variable=gith_choice, onvalue="Gith ",
                         offvalue="", bg='gray80')
gith_check.grid(row=0, column=1)
# GNOLLS #
gnoll_choice = StringVar()
gnoll_check = Checkbutton(human_section, text="Gnoll",
                          variable=gnoll_choice, onvalue="Gnoll ",
                          offvalue="", bg='gray80')
gnoll_check.grid(row=1, column=1)
# GOBLINOIDS #
goblin_choice = StringVar()
goblin_check = Checkbutton(human_section, text="Goblinoid",
                           variable=goblin_choice, onvalue="Goblinoid ",
                           offvalue="", bg='gray80')
goblin_check.grid(row=2, column=1)
# GRUNGS #
grung_choice = StringVar()
grung_check = Checkbutton(human_section, text="Grung",
                          variable=grung_choice, onvalue="Grung ",
                          offvalue="", bg='gray80')
grung_check.grid(row=3, column=1)
# KOBOLDS #
kobold_choice = StringVar()
kobold_check = Checkbutton(human_section, text="Kobold",
                           variable=kobold_choice, onvalue="Kobold ",
                           offvalue="", bg='gray80')
kobold_check.grid(row=4, column=1)
# KUO-TOA #
kuotoa_choice = StringVar()
kuotoa_check = Checkbutton(human_section, text="Kuo-Toa",
                           variable=kuotoa_choice, onvalue="Kuo-Toa ",
                           offvalue="", bg='gray80')
kuotoa_check.grid(row=5, column=1)
# LIZARDFOLK #
lizardfolk_choice = StringVar()
lizardfolk_check = Checkbutton(human_section, text="Lizardfolk",
                               variable=lizardfolk_choice, bg='gray80',
                               onvalue="Lizardfolk ", offvalue="")
lizardfolk_check.grid(row=6, column=1)
# MEAZELS #
meazel_choice = StringVar()
meazel_check = Checkbutton(human_section, text="Meazel",
                           variable=meazel_choice, onvalue="Meazel ",
                           offvalue="", bg='gray80')
meazel_check.grid(row=0, column=2)
# ORCS #
orc_choice = StringVar()
orc_check = Checkbutton(human_section, text="Orc",
                        variable=orc_choice, onvalue="Orc ",
                        offvalue="", bg='gray80')
orc_check.grid(row=1, column=2)
# SAHUAGIN #
sahuagin_choice = StringVar()
sahuagin_check = Checkbutton(human_section, text="Sahuagin",
                             variable=sahuagin_choice, onvalue="Sahuagin ",
                             offvalue="", bg='gray80')
sahuagin_check.grid(row=2, column=2)
# SHADAR-KAI #
shadarkai_choice = StringVar()
shadarkai_check = Checkbutton(human_section, text="Shadar-Kai",
                              variable=shadarkai_choice, bg='gray80',
                              onvalue="Shadar-Kai ", offvalue="")
shadarkai_check.grid(row=3, column=2)
# THRI-KREEN #
thrikreen_choice = StringVar()
thrikreen_check = Checkbutton(human_section, text="Thri-Kreen",
                              variable=thrikreen_choice, bg='gray80',
                              onvalue="Thri-Kreen ", offvalue="")
thrikreen_check.grid(row=4, column=2)
# TROGLODYTES #
troglodyte_choice = StringVar()
troglodyte_check = Checkbutton(human_section, text="Troglodyte",
                               variable=troglodyte_choice, bg='gray80',
                               onvalue="Troglodyte ", offvalue="")
troglodyte_check.grid(row=5, column=2)
# XVARTS #
xvart_choice = StringVar()
xvart_check = Checkbutton(human_section, text="Xvart",
                          variable=xvart_choice, onvalue="Xvart ",
                          offvalue="", bg='gray80')
xvart_check.grid(row=6, column=2)

#################################################################################

### EXECUTION BUTTONS ###

encounter_button = Button(main_window, text='''Create
Encounter''', padx=5, pady=5, command=encounter_display, bd=10, relief=RAISED,
                          bg='black', fg='red')
encounter_button.configure(height=5, width=11, font='Verdana 14 bold')
encounter_button.grid(row=2, column=1)


########################################################################

### FINAL ENCOUNTER SECTION ###
enc_group_frame = LabelFrame(main_window, text="Your Encounter Group",
                             labelanchor='n', font='Verdana 11 bold underline',
                             padx=5, pady=5, bd=15, relief=RIDGE,)
enc_group_frame.grid(row=1, column=2, rowspan=4, sticky=N)

name_label = Label(enc_group_frame, text="Monster Name",
                   font='Verdana 9 bold underline', padx=10)
name_label.grid(row=0, column=0, sticky=W)
hp_label = Label(enc_group_frame, text="HP Total",
                 font='Verdana 9 bold underline', padx=10)
hp_label.grid(row=0, column=1)
ac_label = Label(enc_group_frame, text="AC", font='Verdana 9 bold underline',
                 padx=10)
ac_label.grid(row=0, column=2)
speed_label = Label(enc_group_frame, text="Speed",
                    font='Verdana 9 bold underline', padx=10)
speed_label.grid(row=0, column=3)
book_label = Label(enc_group_frame, text="Book / Page",
                   font='Verdana 9 bold underline', padx=10)
book_label.grid(row=0, column=4)

#########################################################################

### INSTRUCTIONS SECTION ###

instructions_frame = LabelFrame(main_window, labelanchor='n', padx=5, pady=2,
                                text='How to Use Encounter Generator', bd=10,
                                relief=RIDGE, font='Verdana 10 bold underline')
instructions_frame.grid(row=0, column=2)
instruct1 = Label(instructions_frame,
                  text='''1. Input your party's individual levels in the 'XP Thresholds' section, then click 
    'SUBMIT LV' after each entry. Only enter integers, or it won't work!''', justify=LEFT)
instruct1.grid(row=0, column=0, sticky=W)
instruct2 = Label(instructions_frame,
                  text='''2. Once all player levels have been submitted, click 'FINISHED' to see your 
    party's encounter XP thresholds by difficulty.''', justify=LEFT)
instruct2.grid(row=1, column=0, sticky=W)
instruct3 = Label(instructions_frame,
                  text='''3. Select the difficulty, terrain, creature type(s), and min/max XP value of each 
    creature for your encounter. Tip: If you pick a terrain, avoid creature types.''', justify=LEFT)
instruct3.grid(row=2, column=0, sticky=W)
instruct4 = Label(instructions_frame,
                  text='''4. Once all desired parameters for the encounter are selected, click on the 
    'Create Encounter' button for a random encounter!''', justify=LEFT)
instruct4.grid(row=3, column=0, sticky=W)



###WOULD ALSO BE USEFUL TO BUILD A "CLEAR ALL" BUTTON THAT WIPES ALL
###CREATURE, DIFFICULTY AND TERRAIN OPTIONS WITH ONE PUSH, TO SAVE THE USER
###FROM HAVING TO DO THIS MANUALLY EVERY TIME.

main_window.mainloop()



###FOR FINAL READOUT, YOU MIGHT BE ABLE TO USE A MESSAGEBOX, BUT THIS MIGHT
###BE LIMITING AS TO HOW MUCH INFO YOU CAN DISPLAY

###LOOK UP "PYTHON TO EXE.FILE" TO MAKE THIS FILE A CLICK-TO-OPEN FILE.

