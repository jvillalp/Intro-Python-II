from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
room['outside'].items.append(Item("Sword", "Used to kill the spiders."))
room['outside'].items.append(Item("Stick", "used to hit rock."))
room['foyer'].items.append(Item("Rock", "To open doors."))
# Make a new player object that is currently in the 'outside' room.
print("What is your name? ")
name = input()

player = Player(name, room['outside'], [])

# Write a loop that:
user_is_playng = True

while user_is_playng:
    print("Current Room: " + player.current_room.name)
    print("\nDescription: " + player.current_room.description)
    print("\nRoomItems: ")
    for item in player.current_room.items:
        print(item)
    print("\nPlayerItems: ")
    for item in player.items:
        print(item)
    print("\nWhat direction would you like to go? Use N,S,E,W for directions, and q to quit.")
    direction = input()
    currentRoom = player.current_room.name
    if direction.lower() == 'n':
        if player.current_room.n_to:
            player.current_room = player.current_room.n_to
    elif direction.lower() == 's':
        if player.current_room.s_to:
            player.current_room = player.current_room.s_to
    elif direction.lower() == 'e':
        if player.current_room.e_to:
            player.current_room = player.current_room.e_to    
    elif direction.lower() == 'w':
        if player.current_room.w_to:
            player.current_room = player.current_room.w_to
    elif direction.lower() == "q":
        break
    else:
        "Error: Please try again using N, S, E, W, and Q for commands."
    if player.current_room.name == currentRoom:
        print("Cannot go in that direction, please try again.")
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
