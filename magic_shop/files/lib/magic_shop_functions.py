import ast
import os
from random import choice
from tkinter import *

# The function and section of code used in this module opens the magic_item_list and pulls
# its info out for use in the search.


######################################
###   MAGIC ITEM SEARCH FUNCTION   ###
######################################

def magic_item_search(min_gp, max_gp, type, rarity, standard_gp_cost):
    '''Searches for all magic items that meet desired criteria given by user'''

    # Open magic_item_list as string, then convert to dict and add it to variable for use.
    cwd = os.getcwd()
    magic_item_list = cwd + "\\lib\\magic_item_list.txt"
    with open(magic_item_list, 'r') as item_dict:
        magic_items = ast.literal_eval(item_dict.read())

    # Cycle through items to find which ones match the given criteria.
    chosen_items = {}
    for item, info in magic_items.items():  # Target each item to use in for loop
        type_split = info.get("Type").split(" ")
        cost = int(info.get("Cost"))
        # Convert to standard (non-homebrew) cost for magic items
        if standard_gp_cost == True: 
            cost = int(cost / 10)
            info["Cost"] = str(cost)

        if (type_split[0] in type) and int(min_gp) <= cost <= int(max_gp) and \
        (info.get("Rarity") in rarity):
            chosen_items[item] = info

    return chosen_items

####################################
###   ITEM RANDOMIZER FUNCTION   ###
####################################

def item_randomizer(item_list, num_items):
    '''Choose number of items randomly from chosen magic items as many times
       as user wants, then display'''
    magic_shop_items = {}
    item_count = 0
    if num_items > len(item_list.keys()):
        num_items = len(item_list.keys())
    complete = False
    while complete == False:
        random_item = choice(list(item_list.keys()))
        if random_item in magic_shop_items.keys():
            continue
        else:
            magic_shop_items[random_item] = item_list.get(random_item)
            item_count += 1
        if item_count == num_items:
            complete = True

    print("Chosen Items: ", sorted(magic_shop_items.keys()))
    return magic_shop_items

#########################################################
### ITEM DESCRIPTION ON MOUSE HOVER CLASS & FUNCTIONS ###
#########################################################

# Borrowed from https://newbedev.com/display-message-when-hovering-over-something-with-mouse-cursor-in-python

# This nested function creates a ToolTip that can display text
# when hovering over a widget.

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("helvetica", "11", "normal", "italic"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)