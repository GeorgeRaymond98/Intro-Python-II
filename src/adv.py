from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

items = {
    'sword': Item('sword ', 'Golden sword that killed a dragon. Damage:[20]'),
    'mirror': Item('mirror', 'A broken mirror that was brought from the underword. Damage:[0]'),
    'shoes': Item('shoes', 'Gives you movement speed. Damage:[12]'),
    # 'Head of Lavvada': Item('head of lavvada', 'Lavvada was once the most feard kinght. Damage:[50]'),
    'chest': Item('chest', 'Filled with gold')
}

room['outside'].add_item(items['sword'])
room['foyer'].add_item(items['mirror'])
room['overlook'].add_item(items['shoes'])
# room['narrow'].add_item(items['head of lavvada'])
room['treasure'].add_item(items['chest'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


# player1 = Player('player1', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# print(player1.current_room.name)
# * Prints the current description (the textwrap module might be useful here).
# print(player1.current_room.description)
# * Waits for user input and decides what to do.

# print(input)
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

current_room = room["narrow"]

name = input("What's your name?")
player = Player(name, current_room)
describe = f"{player.name}, {current_room}"

player_move = " "
next_room = " "


#         print(
#             "You didn't listen. Enter [N], [S], [E], [W] to move or [q] to Quit: ")
print(f'Welcome {player.name} to {current_room}')
# print(
#     "Listen carefully, Press [N] for North, [S] for South, [E] for East, [W] for West and [q] Quit")


while True:
    player_move = input("Enter [N], [S], [E], [W] to move or [q] to Quit:")
    if player_move.upper() == "N":
        print(f'{player.name} enters {next_room}')
        if player.current_room.n_to != None:
            player.current_room = player.current_room.n_to
            print(
                f'room: {player.current_room.name} \n description: {player.current_room.description}')
        else:
            print(
                'A bolder is blocking this path. You try to me it, but it does not move.')
    elif player_move.upper() == "S":
        print(f'{player.name} enters {next_room}')
        if player.current_room.s_to != None:
            player.current_room = player.current_room.s_to
            print(
                f'room: {player.current_room.name} \n description: {player.current_room.description}')
        else:
            print(
                'A bolder is blocking this path. You try to me it, but it does not move.')
    elif player_move.upper() == "E":
        print(f'{player.name} enters {next_room}')
        if player.current_room.e_to != None:
            player.current_room = player.current_room.e_to
            print(
                f'room: {player.current_room.name} \n description: {player.current_room.description}')
        else:
            print(
                'A bolder is blocking this path. You try to me it, but it does not move.')
    elif player_move.upper() == "W":
        print(f'{player.name} enters {next_room}')
        if player.current_room.w_to != None:
            player.current_room = player.current_room.w_to
            print(
                f'room: {player.current_room.name} \n description: {player.current_room.description}')
        else:
            print(
                'A bolder is blocking this path. You try to me it, but it does not move.')
    elif player_move.upper() == "I":
        if len(player.current_room.items) > 0:
            for i in player.current_room.items:
                print(f'name: {i.name} \n description: {i.description}')

    elif player_move.upper() == "Q":
        print(f'{player.name} is Leaving the game.... See yah!')
        break

