##Ben Sehnert
##8-8-18
##cs172 lab seven

from Room import Room
from Maze import Maze

# how to randomize the directions/ paths
# cannot be purely random- because paths need to be semi intelligent in order to make sense


rooms = []

for i in range(30):
    #not a good use of for loop?
    # no need for incrementing variable ...
    rooms.append(Room())

for i in rooms:
    print(i)

# def set_direction(first, second, choice = ["north", "south", "east", "west"]):
#     if choice == "north":
        

# #room 0 is south of room 1
# my_rooms[0].setNorth(my_rooms[1])
# my_rooms[1].setSouth(my_rooms[0])
# #Room 2 is east of room 1
# my_rooms[1].setEast(my_rooms[2])
# my_rooms[2].setWest(my_rooms[1])
# #room 3 is north of 2
# my_room[3].setSouth(my_rooms[2])
# my_room[2].setNorth(my_rooms[3])
# #room 4 is east of 3
# my_rooms[4].setWest(my_rooms[3])
# my_rooms[3].setEast(my_rooms[4])
# #room 5 is north of 4
# my_rooms[5].setSouth(my_rooms[4])
# my_rooms[4].setWest(my_rooms[5])
# #room 6 is west of 3
# my_rooms[6].setEast(my_rooms[5])
# my_rooms[5].setWest(my_rooms[6])
# #room 7 is west of 6
# my_rooms[7].setEast(my_rooms[6])
# my_rooms[6].setWest(my_rooms[7])
# #room 8 is south of 7
# my_rooms[8].setSouth(my_rooms[7])
# my_rooms[7].setNorth(my_rooms[8])
# #room 9 is west of 7
# my_rooms[9].setEast(my_rooms[2])
# my_rooms[8].setWest(my_rooms[1])
# #room 10 is north 7
# my_rooms[10].setEast(my_rooms[7])
# my_rooms[7].setWest(my_rooms[10])
# #room 11 is west of 10
# my_rooms[1].setEast(my_rooms[2])
# my_rooms[2].setWest(my_rooms[1])
# #room 12 is south of 12
# my_rooms[1].setEast(my_rooms[2])
# my_rooms[2].setWest(my_rooms[1])

# while True:
#     print(my_maze.getCurrent())
#     Pinput = input("Which direction do you want to go?\n")
#     if Pinput == 'North':
#         if my_maze.movenorth():
#             print("you went north")
#         else:
#             print("Invalid direction")
#     elif Pinput == 'South':
#         if my_maze.movesouth():
#             print("you went south")
#         else:
#             print("invalid direction")
#     elif Pinput == 'West':
#         if my_maze.movewest():
#             print("you went west")
#         else:
#             print("Invalid direction")
#     elif Pinput == 'East':
#         if my_maze.moveeast():
#             print("you went east")
#         else:
#             print("invalid direction")
#