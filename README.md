# DND 5e Tools for DMs
This repository contains multiple D&D 5th edition tools that can be used by any DM to make running their game much simpler. These were a labor of love, and in particular the monster encounter randomizer is one of my first Python projects, so apologies if the code is tedious to read through; however, all should function just fine. I hope they aid you as they have helped me! Below I have given a brief description for each tool:

## monster_encounter_randomizer
* Module that uses a collection of methods to take a given number of players and their levels, filter out monsters to meet the DM's criteria, and then output a list of monsters that can be used for a random encounter.
* This module is intended to make building random encounters far more simple than before; instead of having to think through which monsters would apply to a given terrain, calculate their expected difficulty, and then balance to ensure you don't accidentally TPK your party, this tool will handle the bulk of the work for you!
* You can filter out monsters based on various criteria, including terrian, XP value, monster type, and even humanoid variants!
* If you have some homebrewed monsters that you would want to add to this encounter, that is no problem! Simply download the **monster_list_maker_v1.0** script (described below) and use it to include your monsters into the master list of monsters.

## monster_list_maker_v1.0
* Module that allows user to input basic info about a monster into a master dictionary, and then save that dictionary as a text file which can be added to later on.
* This module is intended to be used in conjunction with the monster_encounter_randomizer's master_monster_list.txt, so you can update the master list to include new monsters as future expansions are made for the game we love.

## magic_shop_GUI
* Application that allows the DM to populate a magic item shop with pre-selected items, with prices, book information location, and even descriptions of the items included!
* This module is intended to make life SO much easier for the DM when the party wants to shop for magic items, instead of having to sift through your books to locate each possible item that a party could want, guesstimate what price the item should be, and then find out later you gave them a Cloak of Displacement for WAY below its actual value and made them OP (as I have done...).
* This module allows you to select how many magic items are available at a given store (between 1-20), what types of magic items are available (from ammo and consumables to weapons/armor and wondrous items), rarity of items (Common-Very Rare, with a few less OP Legendary items included with the VR), and finally the expected price range of the items (so your party can reasonably afford those items, or not if you wanna play that way...we all know they can get something like that at the next dungeon if we feel like it ;D).
* Credit is given in the code to the two main sources for this information, but I will post the PDF link from "Sane Magical Prices" where I got the cost balancing of magic items: https://drive.google.com/file/d/0B8XAiXpOfz9cMWt1RTBicmpmUDg/view?resourcekey=0-ceHUken0_UhQ3Apa6g4SJA
