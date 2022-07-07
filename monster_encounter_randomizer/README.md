# monster_encounter_randomizer
* Module that uses a collection of methods to take a given number of players and their levels, filter out monsters to meet the DM's criteria, and then output a list of monsters that can be used for a random encounter.
* This module is intended to make building random encounters far more simple than before; instead of having to think through which monsters would apply to a given terrain, calculate their expected difficulty, and then balance to ensure you don't accidentally TPK your party, this tool will handle the bulk of the work for you!
* You can filter out monsters based on various criteria, including terrian, XP value, monster type, and even humanoid variants!
* If you have some homebrewed monsters that you would want to add to this encounter, that is no problem! Simply download the **monster_list_maker_v1.0** script (described below) and use it to include your monsters into the master list of monsters.

## Current Notes
* Monsters included in this book are from the 5e Monster Manual and Mordenkainen's Tome of Foes; I do not claim any rights to the intellectual property of the monsters or statistics that are included in this application. All of that goes to Wizards of the Coast (love you guys!).
* While I have structured the code to be able to include multiples of monsters (randomized I believe up to 8 of the same monster in an encounter), if the encounter range is too narrow in terms of criteria, it is very possible to end up with ALL of the monsters being multiples of a single type; if you want to submit an adjustment to the code to make this less common, I would be happy to take a look and give you credit!
