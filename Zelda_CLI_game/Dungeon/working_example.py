##Ben Sehnert
##8-8-18
##cs172 lab seven

from Room import Room
from Maze import Maze

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
        set_east(rooms[i], rooms[i+1])
        # prevents top border from being linked to non existent list members.
        if i > size - (row + 1):
            continue
        set_north(rooms[i], rooms[i+6])

def make_move(maze, player_input):
    if player_input == 'north':
        print("You moved north") if maze.move_north(maze.current.north) else print('Invalid direction')
    elif player_input.lower() == 'South':
        print("you went south") if maze.move_south(maze.current.south) else print('invalid direction.')
    elif player_input == 'West':
        print("you went west") if maze.move_west(maze.current.west) else print('Invalid direction.')
    elif player_input == 'East':
        print('You moved east') if maze.move_east(maze.current.east) else print('invalid direction.')

def test(maze = Maze()):
    while True:
        print(maze.current)
        # maze.current.available_moves(maze.current)
        # with that commented out, player can no longer tell which directions can be traveled in.
        make_move(maze, player_input = input("Which direction do you want to go?\n").lower())
        # seems that current never gets changed by player input

test()