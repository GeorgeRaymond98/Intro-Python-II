# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room


class Player:
    def __init__(self, name, room, items=None):
        self.name = name
        self.current_room = room
        self.items = [] if items is None else items

    def move_room(self, new_room):
        self.current_room = new_room

    def change_name(self, name):
        self.name = name

    def __init__(self, name, room):
        self.name = name
        self.current_room = room

    def __str__(self):
        return f"Welcome {self.name} you are in room{self.current_room}"

    def print_items(self):
        if len(self.current_room.items) > 0:
            for i in self.items:
                print(i)
        else:
            print("You thought Wrong! NO item ")
