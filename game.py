#!/usr/bin/python3

from map import places
from player import *
from items import *
from gameparser import *
from enemies import *
import random
import os
import time



def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    string = ""
    for x in items:
        string = string + x["name"]
        if x != items[len(items) - 1]:
            string = string + ", "
    return string
    pass


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(places["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(places["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(places["Robs"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    if list_of_items(room["items"]) != "":
        print("There is " + list_of_items(room["items"]) + " here.")
        print("")
    pass


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(places["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(places["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(places["Robs"])
    <BLANKLINE>
    ROBS' ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Rob Evans and Rob Davies. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    print_room_items(room)

    #
    # COMPLETE ME!
    #

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(places["Reception"]["exits"], "south")
    "Robs' room"
    >>> exit_leads_to(places["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(places["Tutor"]["exits"], "west")
    'Reception'
    """
    return places[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "Robs' room")
    GO SOUTH to Robs' room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to Robs' room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    if current_place == places["Lair"]:
        kraken_fight()
    else:    
        print()
        print("You can:")
        print()
        for direction in exits:
            print_exit(direction, exit_leads_to(exits, direction))
        if current_place["battle"] == True:
            print("Explore the local area.")
        if current_place == places["Gym"]:
            print("Train strength, defence or speed for a cost of 25 gold per stat?")
        if current_place == places["Weapons"] or current_place == places["Armour"]:
            for item in room_items:
                print("BUY " + item["id"] + " for " + str(item["value"]) + ".")
            if weapon[0] != weapon_nothing:
                value = (weapon[0]["value"] * 0.6) % 1
                print("SELL " + weapon[0]["id"] + " for " + str(int((weapon[0]["value"] * 0.6) - value)) + ".")
            if armour[0] != armour_nothing:
                value = (armour[0]["value"] * 0.6) % 1
                print("SELL " + armour[0]["id"] + " for " + str(int((armour[0]["value"] * 0.6) - value)) + ".")
        print()
        print("What do you want to do?")


def kraken_fight():
    if fight_monster(enemy_kraken) == True:
        print("                             _____   ___    ")
        print("\         / | |\   | |\   | |       |   \  |")
        print(" \   ^   /  | | \  | | \  | |___    |___/  |")
        print("  \ / \ /   | |  \ | |  \ | |       |   \  |")
        print("   V   V    | |   \| |   \| |_____  |    \ .")
    else:
        print("")
        print("You wake up a bit disorientated in your own bed with a vague memory of fighting the Kraken.")
        print("You find a note that reads 'Don't be so stupid in future, leave the leviathon alone'.")
        stats["money"] = 0
        current_place = places["Home"]




def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(places["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(places["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(places["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(places["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."

    """
    global current_place
    if is_valid_exit(current_place["exits"], direction) == True:
        current_place = move(current_place["exits"], direction)
    else:
        print("You cannot go there.")
    pass


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    for item in current_place["items"]:
        if item["id"] == item_id:
            if stats["money"] >= item["value"]:
                if item["type"] == "W":
                    if weapon[0] != weapon_nothing:
                        print("You need to sell your current weapon first.")
                    else:
                        weapon_update(item_id, item)
                else:
                    if armour[0] != armour_nothing:
                        print("You need to sell your current armour first.")
                    else:
                        armour_update(item_id, item)
            else:
                print("You don't have enough money for that.")
                return
    print("That isn't in the room.")
    pass

def weapon_update(item_id, item):
    global weapon
    if (stats["mass"] + item["mass"]) <= (stats["strength"] / 5):                
        stats["mass"] =+ item["mass"]
        stats["money"] = stats["money"] - item["value"]
        weapon[0] = item
        current_place["items"].remove(item)
        print("You now have " + str(stats["money"]) + " money.")
        return
    else:
        print("The weight is too much, try dropping someting.")
        return


def armour_update(item_id, item):
    global armour
    if (stats["mass"] + item["mass"]) <= (stats["strength"] / 5):                
        stats["mass"] =+ item["mass"]
        stats["money"] = stats["money"] - item["value"]
        armour[0] = item
        current_place["items"].remove(item)
        print("You now have " + str(stats["money"]) + " money.")
        return
    else:
        print("The weight is too much, try dropping someting.")
        return

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    global weapon
    global armour
    if weapon[0]["id"] == item_id:
        stats["mass"] =- weapon[0]["mass"] 
        value = (weapon[0]["value"] * 0.6) % 1
        stats["money"] = stats["money"] + int((weapon[0]["value"] * 0.6) - value)
        current_place["items"].append(weapon[0])
        weapon[0] = weapon_nothing
        print("You now have " + str(stats["money"]) + " money.")
        return
    elif armour[0]["id"] == item_id:
        stats["mass"] =- armour[0]["mass"] 
        value = (armour[0]["value"] * 0.6) % 1
        stats["money"] = stats["money"] + int((armour[0]["value"] * 0.6) - value)
        current_place["items"].append(armour[0])
        armour[0] = armour_nothing
        print("You now have " + str(stats["money"]) + " money.")
        return
    else:
        print("You don't have that to drop it.")
    pass

def execute_explore():
    global current_place
    print("explore " + current_place["name"])
    if random.randrange(1, 6, 1) < 5:
        enemy = enemy_calculator()
        print("You encounter a random " + enemy["name"])
        result = fight_monster(enemy)
        print("")
        print("You had " + str(stats["money"]) + " gold.")
        if result == True:
            print("You slay the " + enemy["name"] + " and take some money you find near it.")
            stats["money"] = stats["money"] + random.randrange(1, enemy["money"], 1)
        else:
            print("You wake up a bit disorientated in your own bed.")
            print("You have a message that reads 'I found you passed out and bleeding, I looked after you but took payment for this from your possesions.")
            stats["money"] = 0
            current_place = places["Home"]
    else:
        print("You find a random ")
    print("You now have " + str(stats["money"]) + " gold.")


def enemy_calculator():
    if current_place == places["Stream"]:
        enemy = enemy_list[random.randrange(1, 7, 1)]
    elif current_place == places["Forest"]:
        enemy = enemy_list[random.randrange(6, 15, 1)]
    elif current_place == places["Lake"]:
        enemy = enemy_list[random.randrange(6, 28, 1)]
    elif current_place == places["Caves"]:
        enemy = enemy_list[random.randrange(15, 28, 1)]
    elif current_place == places["Knight"]:
        enemy = enemy_list[random.randrange(15, 41, 1)]
    elif current_place == places["Goblin"]:
        enemy = enemy_list[random.randrange(28, 41, 1)]
    elif current_place == places["Deeper"]:
        enemy = enemy_list[random.randrange(41, 50, 1)]
    return enemy
    

    
def execute_train(stat):
    if stats["money"] >= 25:
        stats["money"] = stats["money"] - 25 
        stats[stat] = stats[stat] + 1
        print("You now have " + str(stats[stat]) + " " + stat + " and " + str(stats["money"]) + " money.")
    else:
        print("You don't have enough gold, get out of here.")

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "buy":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("buy what?")

    elif command[0] == "sell":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("sell what?")
    elif command[0] == "explore" and current_place["battle"] == True:
        execute_explore()
    elif command[0] == "train" and current_place == places["Gym"]:
        if len(command) > 1:
            execute_train(command[1])
        else:
            print("Train what?")
    else:
        print("This makes no sense.")

def fight_monster(enemy):
    e_health = enemy["health"]
    p_health = stats["health"]
    counter = 0
    p_counter = 0
    e_counter = 0
    while e_health > 0 and p_health > 0:
        enemy_speed = random.randrange(enemy["speed"], enemy["speed"] * 2, 1)
        player_speed = random.randrange(stats["speed"], stats["speed"] * 2, 1)
        counter = counter + 1
        if enemy_speed > player_speed:
            e_counter = e_counter + 1
            damage = enemy["strength"] - stats["defence"] - armour[0]["defence"]
            if damage > 0:
                p_health = p_health - damage
                print(enemy["name"] + " hits you for " + str(damage) + " damage. You have " + str(p_health) + " health remaining.")
        else:
            p_counter = p_counter + 1
            damage = (stats["strength"] - enemy["defence"] + weapon[0]["damage"])
            if damage > 0:
                e_health = e_health - damage
                print("You hit the enemy for " + str(damage) + " damage. The enemy has " + str(e_health) + " health remaining.")
        if counter == 101:
            print("The fight takes it's toll on both of you and you just lie there bleeding out, but who will bleed out quicker?")
            if p_counter > e_counter:
                return(True)
            else:
                return(False)
    if e_health > 0:
        return(False)
    else:
        return(True)




def menu(exits, room_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    os.system('cls' if os.name == 'nt' else 'clear')

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(places["Reception"]["exits"], "south") == places["Robs"]
    True
    >>> move(places["Reception"]["exits"], "east") == places["Tutor"]
    True
    >>> move(places["Reception"]["exits"], "west") == places["Office"]
    False
    """

    # Next room to go to
    return places[exits[direction]]

def print_game_menu():
    print()
    print()
    print()
    print('{:^80}'.format("Start Game - Press 1"))
    print()
    print('{:^80}'.format("Score Board - Press 2"))
    print()
    print('{:^80}'.format("How to play - Press 3"))
    print()
    print('{:^80}'.format("Exit - Press 4"))
    print()
    user_choice = input("Press a Number and hit ENTER . . . ")
    return user_choice

def print_score_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print('{:^80}'.format("Here is the score board"))
    print()
    user_choice = input("Press key to return to menu . . . ")
    return

def print_rules():
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print('{:^80}'.format("Here are the rules"))
    print()
    user_choice = input("Press key to return to menu . . . ")
    return

def exit_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print('{:^80}'.format("GOOD BYE"))
    print()
    time.sleep(1)
    return


# This is the entry point of our program
def main():

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        option = print_game_menu()
        if option == "1":
            break;
        if option == "2": 
            print_score_board()
        if option == "3": 
            print_rules()
        if option == "4": 
            exit_game()
            return


    os.system('cls' if os.name == 'nt' else 'clear') 

    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_place)

        # Show the menu with possible actions and ask the player
        command = menu(current_place["exits"], current_place["items"])

        # Execute the player's command
        execute_command(command)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

