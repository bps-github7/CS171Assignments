##Ben Sehnert
##8-8-18
##cs172 lab seven

from Room import Room
from Maze import Maze

# how to randomize the directions/ paths
# cannot be purely random- because paths need to be semi intelligent in order to make sense


rooms = []

for i in range(36):
    d = Room()
    rooms.append(d)

# for elements in rooms:
#     print(elements)

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

# im sure there is some way to do this in one go. experiment around a bit

for i in range(0,36):
    if i % 6 == 0:
        continue
    #i think that does it, but need to validate
    set_east(rooms[i], rooms[i+1])
    set_north(rooms[i], rooms[i+6])


# #first row east to west
# for i in range(0,6):
#     set_east(rooms[i], rooms[i+1])


# #second row east to west
# for i in range(6, 11):
#     set_east(rooms[i], rooms[i+1])

# #third row east to west
# for i in range(11, 17):
#     set_east(rooms[i], rooms[i+1])

# # fourth row east to west
# for i in range(17, 23):
#     set_east(rooms[i], rooms[i+1])

# # fifth row east to west
# for i in range(23, 29):
#     set_east(rooms[i], rooms[i+1])

# # sixth row east to west
# for i in range(29, 36):
#     set_east(rooms[i], rooms[i+1])


# while True:
#     print(maze.getCurrent())
#     Pinput = input("Which direction do you want to go?\n")
#     if Pinput == 'North':
#         if maze.movenorth():
#             print("you went north")
#         else:
#             print("Invalid direction")
#     elif Pinput == 'South':
#         if maze.movesouth():
#             print("you went south")
#         else:
#             print("invalid direction")
#     elif Pinput == 'West':
#         if maze.movewest():
#             print("you went west")
#         else:
#             print("Invalid direction")
#     elif Pinput == 'East':
#         if maze.moveeast():
#             print("you went east")
#         else:
#             print("invalid direction")
#