'''
Module Level Docstring:
Implements 
'''
from Room import Room

class Maze:
    '''Class Level Docstring:'''
    version = 2.0
    def __init__(self,st,ex = Room()):
        self.start = Room()
        self.exit = ex
        self.current = st
    
    def at_exit(self):
        return True if self.current == self.exit else False

    def reset(self):
        self.current = self.start

    # if current room has a room 
    # in the intended movement direction, then
    # change the current room to other_room: 
    #  -> (reference to new Room object)
    # if there isnt a room, return False
    # because we cant move in this direction.

    def move_north(self, other_room):
        if self.current.north:
            self.current = other_room
            return True
        else:
            return False

    def move_south(self, other_room):
        if (self.current.south):
            self.current = other_room
            return True
        else:
            return False

    def move_east(self, other_room):
        if (self.current.east):
            self.current = other_room
            return True
        else:
            return False

    def move_west(self, other_room):
        if (self.current.west):
            self.current = other_room
            return True
        else:
            return False