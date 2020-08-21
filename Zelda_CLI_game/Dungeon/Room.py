'''Module Level docstring:

'''

#qyeing up folder in system path for import statements below.
import sys
sys.path.insert(0, 'C:\\Users\\Ben\\vscodeSCM\\CS171Assignments\\Zelda_CLI_game\\Enemies')


from Bokoblin import Bokoblin
from Chuchu import Chuchu
from Moblin import Moblin
from Darknut import Darknut
import random

# Idea for moving back and fourth between previous rooms-
# pass alt constructor previous rooms' repr method

# #     @classmethod
    # def from_repr(cls, arg):
    #     '''sort of unpythonic, but expected 
    #     use case is only within this class'''
    #     return Room(**arg)
    # 
    # 
    # def travel(self):
    #     while True:
    #         print("Which room would you like to travel to?")
    #         for i in ("east", "north", "west"):
    #             print(i)
    #         direction = input().lower() 
    #         if direction not in ("north","west","east"):
    #             print("not a valid choice! try again")
    #             continue
    #         break
    #     print("You chose to move",direction)
    #     return Dungeon(previous = self.__repr__(), count = (self.count + 1))

    # def travel_back(self):
    #     return Dungeon(previous = self.__repr__(), current = Room.from_repr(self.previous.__repr__()), count = (self.count + 1))



def create_opponent():
    '''Creates a random monster with a random name'''
    monsters = ["Chuchu","Bokoblin","Moblin","Darknut"]
    names = []
    # not very reusable: consider other users environments...
    with open(r'C:\Users\Ben\vscodeSCM\CS171Assignments'
    r'\Zelda_CLI_game\Dungeon\assets\opponents.txt') as file:
        for lines in file:
            names.append(lines.strip('\n'))
    return eval("{}('{}')".format(random.choice(monsters),
    random.choice(names)))

#make these create_room_name, Create_room_desc, create_reward
# more inline with what the function does, and looks better.
def create_room_name():
    '''returns a random room name.
    Those prepended with * will end the game
    if dungeon.count > 10'''
    room_names = []
    # not very reusable: consider other users environments...
    with open(r'C:\Users\Ben\vscodeSCM\CS171Assignments'
    r'\Zelda_CLI_game\Dungeon\assets\room_names.txt') as file:
        for lines in file:
            room_names.append(lines.strip('\n'))    
    name = random.choice(room_names)
    return name.title()

def create_room_desc():
    descriptions = []
    # not very reusable: consider other users environments...
    with open(r'C:\Users\Ben\vscodeSCM\CS171Assignments'
    r'\Zelda_CLI_game\Dungeon\assets\room_desc.txt') as file:
        contents = file.read()
        for lines in contents.split('/'):
            descriptions.append(lines.strip('\n'))
    return random.choice(descriptions)

def create_reward():
    '''Decides if a room contains a reward. less than favoraable odds'''
    return 1 if random.random() < .2 else 0

class Room:
    '''Class Docstring:
    
    '''
    version = 2.0
    count = 0

    def __init__(self):
        '''1) these arent truly random because its not guranteed
        that random.choice wont pick the same name from a list twice
        on seperate iterations- so figure out how to 
        (non-permanently) delete an entry after reading from it
        2) ^^^ would be a nice touch ^^^ '''
        self.name = create_room_name()
        self.description = create_room_desc()
        self.enemy = create_opponent()
        self.reward = create_reward()
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        # #so that we know when a certain number of rooms
        # have been navigated to... do something with count.
        # maybe in a different method.. 
        # Room.count += 1

    def __str__(self):
        return "Room Name: {}\n\
        \r\rDescription: {}\n\
        \r\rEnemy: {}\n\
        \r\rReward: {}"\
        .format(self.name, self.description,
        self.enemy, ("Yes" if self.reward else "No"))
    
    def __repr__(self):
        return {"name": self.name, "description" : self.description,
        "enemy": self.enemy, "reward" : self.reward}

    def available_moves(self):
        '''Simple interface for printing 
        available moves from the current one.
        (ie. which rooms border this room)'''
        if self.north:
            print('north ^')
        if self.south:
            print('south v')
        if self.east:
            print('east  >')
        if self.west:
            print('west  <')


    @classmethod
    def from_repr(cls, arg):
        '''sort of unpythonic, but expected 
        use case is only within this class'''
        return Room(**arg)

print(create_room_desc())