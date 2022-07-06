from lib import magic_shop_functions as msf
from tkinter import *

##############
# User Input #
##############

normal_DND_cost = True

#########################
### FUNCTIONS SECTION ###
#########################

def run_magic_shop():
    '''This function runs the basic search and randomization
       of chosen items, and then sets these into the "SHOP ITEMS"
       frame with info in appropriate sections, sans description.'''
    
    # Take all needed variables and set to global
    global ammo_choice, armor_choice, instrument_choice, potion_choice
    global ring_choice, rod_choice, scroll_choice, shield_choice, staff_choice
    global wand_choice, weapon_choice, wondrous_choice, common_magic_choice
    global uncommon_magic_choice, rare_magic_choice, v_rare_magic_choice
    global max_price_spinbox, min_price_spinbox, num_items_spinbox
    global previous_shop_frame

    # Set the lists based on chosen parameters for magic item search.
    type_selection = [ammo_choice.get(), armor_choice.get(), \
                      instrument_choice.get(), potion_choice.get(), \
                      ring_choice.get(), rod_choice.get(), \
                      scroll_choice.get(), shield_choice.get(), \
                      staff_choice.get(), wand_choice.get(), \
                      weapon_choice.get(), wondrous_choice.get()]

    rarity_selection = [common_magic_choice.get(), uncommon_magic_choice.get(), \
                    rare_magic_choice.get(), v_rare_magic_choice.get()]
    
    max_cost = int(max_price_spinbox.get())
    min_cost = int(min_price_spinbox.get())
    num_items = int(num_items_spinbox.get())
    # Run the magic_shop_functions using given parameters and lists.
    try:
        approved_items = msf.magic_item_search(min_gp=min_cost, max_gp=max_cost,
                                           type=type_selection, 
                                           rarity=rarity_selection, 
                                           standard_gp_cost=normal_DND_cost)
        shop_items = msf.item_randomizer(approved_items, num_items)

    # If criteria are not met, send a message informing user and end function.
    except IndexError:
        no_choice_frame = Label(main_window, text=
        '''There are no items that match your criteria.
        Please widen your criteria by type, rarity, or
        cost range and try again.''')
        no_choice_frame.configure(bg="magenta4", fg="floral white",
                                  font=("Book Antiqua", "10", "bold"),
                                  padx=10, pady=10)
        no_choice_frame.grid(row=3, column=1)
        return

    #  Create the "SHOP ITEMS" frame to take right side of app window.
    avail_items_frame = LabelFrame(main_window, text="SHOP ITEMS", bd=0, 
                                   padx=5, pady=5, labelanchor="n")
    avail_items_frame.configure(bg="magenta4", fg="yellow", 
                                font=("Book Antiqua", "20", "bold", "italic",
                                UNDERLINE))                                
    avail_items_frame.grid(row=0, column=2, rowspan=4, sticky="n")

    # Fill in info section labels to line top of SHOP ITEMS frame.
    item_name = Label(avail_items_frame, text="Item Name")
    item_name.configure(bg="magenta4", fg="yellow2", font=("Book Antiqua",
                        "14", "bold", UNDERLINE), pady=5)
    item_rarity = Label(avail_items_frame, text="Rarity")
    item_rarity.configure(bg="magenta4", fg="yellow2", font=("Book Antiqua",
                          "14", "bold", UNDERLINE), pady=5)
    item_type = Label(avail_items_frame, text="Type")
    item_type.configure(bg="magenta4", fg="yellow2", font=("Book Antiqua",
                        "14", "bold", UNDERLINE), pady=5)
    item_attune = Label(avail_items_frame, text="Attunement")
    item_attune.configure(bg="magenta4", fg="yellow2", font=("Book Antiqua",
                          "14", "bold", UNDERLINE), pady=5)
    item_cost = Label(avail_items_frame, text="Cost(gp)")
    item_cost.configure(bg="magenta4", fg="yellow2", font=("Book Antiqua",
                        "14", "bold", UNDERLINE), pady=5)
    item_book = Label(avail_items_frame, text="Book Ref.")
    item_book.configure(bg="magenta4", fg="yellow2", font=("Book Antiqua",
                        "14", "bold", UNDERLINE), pady=5)

    item_name.grid(row=0, column=0, sticky="nesw")
    item_rarity.grid(row=0, column=1, sticky="nesw")
    item_type.grid(row=0, column=2, sticky="nesw")
    item_attune.grid(row=0, column=3, sticky="nesw")
    item_cost.grid(row=0, column=4, sticky="nesw")
    item_book.grid(row=0, column=5, sticky="nesw")

    # Create rows for each item from shop items and fill in.
    shopitem_counter = 1

    for item, info in shop_items.items():
        shopitem_name = Label(avail_items_frame, text=item, )
        shopitem_name.configure(bg="magenta4", fg="IndianRed1", 
                                font=("Book Antiqua", "12", "bold", UNDERLINE))
        shopitem_rarity = Label(avail_items_frame, text=info.get("Rarity"))
        shopitem_rarity.configure(bg="magenta4", fg="floral white", 
                                  font=("Book Antiqua", "11"))
        shopitem_type = Label(avail_items_frame, text=info.get("Type"))
        shopitem_type.configure(bg="magenta4", fg="floral white", 
                                font=("Book Antiqua", "11"))
        shopitem_attune = Label(avail_items_frame, text=info.get("Attunement"))
        shopitem_attune.configure(bg="magenta4", fg="floral white", 
                                  font=("Book Antiqua", "11"))
        shopitem_cost = Label(avail_items_frame, text=info.get("Cost"))
        shopitem_cost.configure(bg="magenta4", fg="floral white", 
                                font=("Book Antiqua", "11"))
        shopitem_book = Label(avail_items_frame, text=info.get("Book"))
        shopitem_book.configure(bg="magenta4", fg="floral white", 
                                font=("Book Antiqua", "11"))
        
        msf.CreateToolTip(widget=shopitem_name, text=info.get("Description"))

        shopitem_name.grid(row=shopitem_counter, column=0)
        shopitem_rarity.grid(row=shopitem_counter, column=1)
        shopitem_type.grid(row=shopitem_counter, column=2)
        shopitem_attune.grid(row=shopitem_counter, column=3)
        shopitem_cost.grid(row=shopitem_counter, column=4)
        shopitem_book.grid(row=shopitem_counter, column=5)

        shopitem_counter += 1

### END OF FUNCTIONS SECTION ###

###############################################################################

#######################
###   GUI SECTION   ###
#######################

main_window = Tk()
main_window.title("Magic Item Shop v2.0")
main_window.configure(bg="magenta4", padx=5, pady=5)

######################################

### Intro Frame ###

intro_label = Label(main_window, text=
'''Welcome to the Magic Shop! This app is designed to
randomly provide a number of 5e magical items that
your players can choose to purchase whenever they
enter a store with magic items. Simply select what 
item rarities, types, and prices that either the store
provides or the players want, and how many options
you want to be offered, and voila! Hope this helps!''',)
intro_label.configure(bg="magenta4", fg="floral white",
                      font=("Book Antiqua", "11", "bold"),
                      padx=10, pady=10,)
intro_label.grid(row=0, column=0, )

######################################

### Num of Items Frame ###

num_items_frame = LabelFrame(main_window, text="Number of Items", bd=0,
                             padx=2, labelanchor="n")
num_items_frame.configure(bg="magenta4", fg="yellow", font=("Book Antiqua",
                          "14", "bold", UNDERLINE, ))
num_items_frame.grid(row=1, column=1,)

num_items_label = Label(num_items_frame, 
                        text="How many magic items do you want?")
num_items_label.configure(bg="magenta4", fg="floral white", 
                          font=("Book Antiqua", "11", "bold",))
num_items_label.grid(row=0, column=0)
num_items_spinbox = Spinbox(num_items_frame, from_=1, to=20, width=3,
                            bg="LightGoldenrod1",  justify="center",
                            font=("Book Antiqua", "11", "bold"))
num_items_spinbox.grid(row=0, column=1)
num_items_var = num_items_spinbox.get() # This is a string value

######################################

### Item Rarity Frame ###

rarity_frame = LabelFrame(main_window, text="ITEM RARITY", padx=5, pady=5,
                          bd=0, labelanchor="n")
rarity_frame.configure(bg="magenta4", fg="yellow", 
                       font=("Book Antiqua", "14", "bold", UNDERLINE))
rarity_frame.grid(row=1, column=0,)

common_magic_choice = StringVar()
common_magic_check = Checkbutton(rarity_frame, text="Common", 
                                 variable=common_magic_choice, 
                                 onvalue="Common", offvalue="", )
common_magic_check.configure(bg="magenta4", fg="floral white", 
                             selectcolor="gray30", 
                             font=("Book Antiqua", "11",))

uncommon_magic_choice = StringVar()
uncommon_magic_check = Checkbutton(rarity_frame, text="Uncommon",
                                   variable=uncommon_magic_choice, 
                                   onvalue="Uncommon", offvalue="",)
uncommon_magic_check.configure(bg="magenta4", fg="floral white", 
                               selectcolor="gray30", 
                               font=("Book Antiqua", "11",))

rare_magic_choice = StringVar()
rare_magic_check = Checkbutton(rarity_frame, text="Rare",
                                   variable=rare_magic_choice, 
                                   onvalue="Rare", offvalue="",)
rare_magic_check.configure(bg="magenta4", fg="floral white", 
                           selectcolor="gray30", 
                           font=("Book Antiqua", "11",))  

v_rare_magic_choice = StringVar()
v_rare_magic_check = Checkbutton(rarity_frame, text="Very Rare",
                                   variable=v_rare_magic_choice, 
                                   onvalue="Very Rare", offvalue="",)
v_rare_magic_check.configure(bg="magenta4", fg="floral white", 
                             selectcolor="gray30", 
                             font=("Book Antiqua", "11",))

common_magic_check.grid(row=0, column=0, sticky="w")
uncommon_magic_check.grid(row=0, column=1, sticky="w")
rare_magic_check.grid(row=1, column=0, sticky="w")
v_rare_magic_check.grid(row=1, column=1, sticky="w")                                                                   

# Set rarity checkbuttons to "On" by default
common_magic_check.select()
uncommon_magic_check.select()
rare_magic_check.select()
v_rare_magic_check.select()

######################################

### Item Type Frame ###

type_frame = LabelFrame(main_window, text="ITEM TYPES", padx=5, pady=5,
                        bd=0, labelanchor="n")
type_frame.configure(bg="magenta4", fg="yellow", 
                     font=("Book Antiqua", "14", "bold", UNDERLINE))
type_frame.grid(row=0, column=1, sticky="nsew" )

ammo_choice = StringVar()
ammo_check = Checkbutton(type_frame, text="Ammunition", variable=ammo_choice, 
                         onvalue="Ammunition", offvalue="", )
ammo_check.configure(bg="magenta4", fg="floral white", 
                     selectcolor="gray30", font=("Book Antiqua", "11",))                                 

armor_choice = StringVar()
armor_check = Checkbutton(type_frame, text="Armor", variable=armor_choice, 
                          onvalue="Armor", offvalue="", )
armor_check.configure(bg="magenta4", fg="floral white", 
                      selectcolor="gray30", font=("Book Antiqua", "11",))

instrument_choice = StringVar()
instrument_check = Checkbutton(type_frame, text="Instrument", 
                               variable=instrument_choice, 
                               onvalue="Instrument", offvalue="", )                                
instrument_check.configure(bg="magenta4", fg="floral white", 
                           selectcolor="gray30", font=("Book Antiqua", "11",))

potion_choice = StringVar()
potion_check = Checkbutton(type_frame, text="Potion", variable=potion_choice, 
                           onvalue="Potion", offvalue="", )
potion_check.configure(bg="magenta4", fg="floral white", 
                       selectcolor="gray30", font=("Book Antiqua", "11",))

ring_choice = StringVar()
ring_check = Checkbutton(type_frame, text="Ring", variable=ring_choice, 
                         onvalue="Ring", offvalue="", )
ring_check.configure(bg="magenta4", fg="floral white", 
                     selectcolor="gray30", font=("Book Antiqua", "11",))

rod_choice = StringVar()
rod_check = Checkbutton(type_frame, text="Rod", variable=rod_choice, 
                        onvalue="Rod", offvalue="", )   
rod_check.configure(bg="magenta4", fg="floral white", 
                    selectcolor="gray30", font=("Book Antiqua", "11",))

scroll_choice = StringVar()
scroll_check = Checkbutton(type_frame, text="Scroll", variable=scroll_choice, 
                           onvalue="Scroll", offvalue="", )
scroll_check.configure(bg="magenta4", fg="floral white", 
                       selectcolor="gray30", font=("Book Antiqua", "11",))                                

shield_choice = StringVar()
shield_check = Checkbutton(type_frame, text="Shield", variable=shield_choice, 
                           onvalue="Shield", offvalue="", ) 
shield_check.configure(bg="magenta4", fg="floral white", 
                       selectcolor="gray30", font=("Book Antiqua", "11",))

staff_choice = StringVar()
staff_check = Checkbutton(type_frame, text="Staff", variable=staff_choice, 
                          onvalue="Staff", offvalue="", )
staff_check.configure(bg="magenta4", fg="floral white", 
                      selectcolor="gray30", font=("Book Antiqua", "11",))

wand_choice = StringVar()
wand_check = Checkbutton(type_frame, text="Wand", variable=wand_choice, 
                         onvalue="Wand", offvalue="", )
wand_check.configure(bg="magenta4", fg="floral white", 
                     selectcolor="gray30", font=("Book Antiqua", "11",))

weapon_choice = StringVar()
weapon_check = Checkbutton(type_frame, text="Weapon", variable=weapon_choice, 
                           onvalue="Weapon", offvalue="", )  
weapon_check.configure(bg="magenta4", fg="floral white", 
                       selectcolor="gray30", font=("Book Antiqua", "11",))

wondrous_choice = StringVar()
wondrous_check = Checkbutton(type_frame, text="Wondrous Item", 
                             variable=wondrous_choice, onvalue='Wondrous',
                             offvalue="", )
wondrous_check.configure(bg="magenta4", fg="floral white", 
                         selectcolor="gray30", font=("Book Antiqua", "11",))

ammo_check.grid(row=0, column=0, sticky="w") 
armor_check.grid(row=0, column=1, sticky="w")                                 
instrument_check.grid(row=0, column=2, sticky="w")                                 
potion_check.grid(row=1, column=0, sticky="w")                                 
ring_check.grid(row=1, column=1, sticky="w") 
rod_check.grid(row=1, column=2, sticky="w")                                
scroll_check.grid(row=2, column=0, sticky="w")                                 
shield_check.grid(row=2, column=1, sticky="w")                                 
staff_check.grid(row=2, column=2, sticky="w")                                 
wand_check.grid(row=3, column=0, sticky="w")                                 
weapon_check.grid(row=3, column=1, sticky="w")                                 
wondrous_check.grid(row=3, column=2, sticky="w")

#Set type checkbuttons to default to "On"
ammo_check.select()
armor_check.select()
instrument_check.select()
potion_check.select()
ring_check.select()
rod_check.select()
scroll_check.select()
shield_check.select()
staff_check.select()
wand_check.select()
weapon_check.select()
wondrous_check.select()

######################################

### Price Range Frame ###

price_frame = LabelFrame(main_window, text="PRICE RANGE", padx=5, pady=5,
                         bd=0, labelanchor="n")
price_frame.configure(bg="magenta4", fg="yellow", 
                      font=("Book Antiqua", "14", "bold", UNDERLINE))
price_frame.grid(row=2, column=0,)

min_price_label = Label(price_frame, text="Minimum cost (gp):")
min_price_label.configure(bg="magenta4", fg="floral white", 
                          font=("Book Antiqua", "11", "bold",))
min_price_label.grid(row=0, column=0)
min_price_spinbox = Spinbox(price_frame, from_=0, to=9999999, width=8,
                            bg="LightGoldenrod1", justify="center", 
                            font=("Book Antiqua", "11", "bold"))
min_price_spinbox.grid(row=0, column=1)
min_price_var = min_price_spinbox.get() # This is a string value

default_max = IntVar()
default_max.set(9999999)
max_price_label = Label(price_frame, text="Maximum cost (gp):")
max_price_label.configure(bg="magenta4", fg="floral white", 
                          font=("Book Antiqua", "11", "bold",))
max_price_label.grid(row=1, column=0)
max_price_spinbox = Spinbox(price_frame, from_=1, to=9999999, width=8, 
                            textvariable=default_max, bg="LightGoldenrod1", 
                            justify="center",
                            font=("Book Antiqua", "11", "bold"))
max_price_spinbox.grid(row=1, column=1)
max_price_var = max_price_spinbox.get() # This is a string value

######################################

### Final Elements ###

# Create instance of SHOP ITEMS frame
avail_items_frame = LabelFrame(main_window, text="SHOP ITEMS", bd=2, 
                               padx=5, pady=5)
avail_items_frame.grid(row=0, column=2, rowspan=4)

# Run_Magic_Shop Button 
run_button = Button(main_window, text="Go Shopping!", command=run_magic_shop)
run_button.configure(bg="firebrick1", fg="floral white", relief="raised",
                     bd=8, font=("Book Antiqua", "28", "bold", "italic",
                     UNDERLINE),)
run_button.grid(row=2, column=1, sticky="nesw")


# Execute Magic Shop Window
main_window.mainloop()

### END OF GUI SECTION ###

##############################################################################

# (TODO) Down the line, it would also be useful to do an "item search" that allows
# searching by specific item name, and possibly even an item description
# that automatically comes with the item so the user can see what exactly the
# item does as well as what it should be worth.

