'''
Module Level Docstring:
Implements 
'''
from Room import Room

class Maze:
    '''Class Level Docstring:'''
    version = 2.0
    def __init__(self, st = Room(), ex = Room()):
        self.start = st
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

rooms = []
for i in range(36):
    d = Room()
    rooms.append(d)

def set_north(room, border):
    room.north = border
    border.south = room

def set_south(room, border):
    room.south = border
    border.north = room

def set_east(room, border):
    room.east = border
    border.west = room

def set_west(room, border):
    room.west = border
    border.east = room

# writing the comments as room 1 = rooms[0] : literal room is list index + 1
# for the sake of readability/ comprehension


### Creating the bottom row for starters, 6 rooms across...
# room 31 | room 32| room 33| room 34| room 35| room 36 |
#| room 25| room 26| room 27| room 28| room 29| room 30 |
#| room 19| room 20| room 21| room 22| room 23| room 24 |
#| room 13| room 14| room 15| room 16| room 17| room 18 |
#| room 7 | room 8 | room 9 | room 10| room 11| room 12 |
#| room 1 | room 2 | room 3 | room 4 | room 5 |  room 6 | 

def create_maze(size = 36, row = 6):
    for i in range(0,size):
        # prevents level 1 right border from linking to level 2 left border
        if i % row == 0:
            continue
        # prevents last room in maze (room 36) from trying to link to non existent list members
        if i == size-1:
            break
        set_east(rooms[i], rooms[i+1])
        # prevents top border from being linked to non existent list members.
        if i > size - (row + 1):
            continue
        set_north(rooms[i], rooms[i+6])

def make_move(maze, player_input):
    if player_input in ('north','^') and maze.move_north(maze.current.north):
        print('You went north.\n')
    elif player_input.lower() in ('south','v') and maze.move_south(maze.current.south):
        print("You went south.\n")
    elif player_input in ('west','<') and maze.move_west(maze.current.west):
        print("You went west.\n")
    elif player_input in ('east','>') and maze.move_east(maze.current.east):
        print('You moved east.\n')
    else:
        print('Invalid direction.')
    # if, elif returns new maze- where current is set new room.
    # else returns the same maze (and current room) that was passed in.
    return maze

def navigate(maze = Maze(st = rooms[2])):
    '''Handles the mechanism of trabeling
    from room to room. using a while loop
    may need to reconfigure this, so that it returns something
    otherwise, it might be hard to reach inside and fight monster
    lot of syntax sugar'''
    while True:
        print(maze.current)
        print("\n\navailable moves:")
        maze.current.available_moves()
    
        maze = make_move(maze, player_input = input("Which direction do you want to go? ").lower())

def main():
    create_maze()
    navigate()

# main()

if __name__ == "__main__":
    m = Maze()
    m.current.south = Room()
    m.current.south = Room()
    print(m.current.south)