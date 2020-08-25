'''Module Level Docstring: 
Programmer: Ben Sehnert
Program: Zelda Command line Mini-game
Date: 8/15/2020

'''
import time
import random
import sys
sys.path.insert(0, r'C:\Users\Ben\vscodeSCM\CS171Assignments\Zelda_CLI_game')
from Hero import Hero
sys.path.insert(0, r'C:\Users\Ben\vscodeSCM\CS171Assignments\Zelda_CLI_game\Enemies')
from Bokoblin import Bokoblin
from Chuchu import Chuchu
from Darknut import Darknut
from Moblin import Moblin
sys.path.insert(0, r'C:\Users\Ben\vscodeSCM\CS171Assignments\Zelda_CLI_game\Dungeon')
from Maze import Maze

def intro():
    '''Start screen- first thing user sees'''
    print(r'''                                    /@
                     __        __   /\/
                    /==\      /  \_/\/   
                  /======\    \/\__ \__
                /==/\  /\==\    /\_|__ \
             /==/    ||    \=\ / / / /_/
           /=/    /\ || /\   \=\/ /     
        /===/   /   \||/   \   \===\
      /===/   /_________________ \===\
   /====/   / |                /  \====\
 /====/   /   |  _________    /  \   \===\    THE LEGEND OF 
 /==/   /     | /   /  \ / / /  __________\_____      ______       ___
|===| /       |/   /____/ / /   \   _____ |\   /      \   _ \      \  \
 \==\             /\   / / /     | |  /= \| | |        | | \ \     / _ \
 \===\__    \    /  \ / / /   /  | | /===/  | |        | |  \ \   / / \ \
   \==\ \    \\ /____/   /_\ //  | |_____/| | |        | |   | | / /___\ \
   \===\ \   \\\\\\\/   /////// /|  _____ | | |        | |   | | |  ___  |
     \==\/     \\\\/ / //////   \| |/==/ \| | |        | |   | | | /   \ |
     \==\     _ \\/ / /////    _ | |==/     | |        | |  / /  | |   | |
       \==\  / \ / / ///      /|\| |_____/| | |_____/| | |_/ /   | |   | |
       \==\ /   / / /________/ |/_________|/_________|/_____/   /___\ /___\
         \==\  /               | /==/
         \=\  /________________|/=/    COMMAND LINE EDITION
           \==\     _____     /==/ 
          / \===\   \   /   /===/
         / / /\===\  \_/  /===/
        / / /   \====\ /====/
       / / /      \===|===/
       |/_/         \===/
                      =''')
    print("{:=^98s}".format("Welcome to Legend of Zelda: Python Edition"))

def create_player():
    '''
returns default player named link
if the user didnt enter anything in prompt.
    '''
    player_name = input("Enter your name(default = Link): ")
    return Hero("link") if player_name in (""," ","\n", " \n") else Hero(player_name)

def triforce():
    print(r"""
               /\
              /  \
             /    \
            /      \
           /        \
          /__________\
         /\__________/\
        /  \        /  \
       /    \      /    \
      /      \    /      \
     /        \  /        \
    /__________\/__________\
    \__________/\__________/""")
    return 0

def game_intro():
    time.sleep(3.0)
    print("You are exploring deep in the dark forbidden woods,\n\n\
    \n\nSent by the Greak Deku tree to rescue a Korok called Makar...\n\n")
    time.sleep(3.0)
    print("out of nearby bushes you hear a shufflin of brushes'\n\n")
    time.sleep(3.0)
    print("You look closely and realize it be monsters...")
    return 0

# def navigate(name, maze = Maze(st = rooms[2])):
#     '''prototype for making move'''
#     while True:
#         print(maze.current)
#         print("\n\navailable moves:")
#         maze.current.available_moves()
#         monster = maze.current.opponent
#         link = Hero(name)
#         zelda_battle(link, monster)
#         maze = Maze.make_move(maze, player_input = input("Which direction do you want to go? ").lower())

def main():
    ''''''
    intro()
    triforce()
    Maze.create_maze()
    link = create_player()

def elixer(attacker):
    attacker.elixer()
    print("{}\n{} elixers remaining".format(attacker.elixer_name(), attacker.elixer_count()))
    print("you now have: {} health points.".format(attacker.get_health()))
    return 1

def arrow(attacker, defender):
    attacker.use_arrow(defender)
    print(attacker.arrow_name())
    print("Your foe has {} health points remaining".format(defender.get_health()))
    print("you have {} arrows left".format(attacker.arrow_count()))
    return 1

def special_hero_move(attacker, defender, attack):
    if attack == "elixer":
        return elixer(attacker)
    elif attack == "arrow":
        return arrow(attacker, defender)


def attack(attacker, defender, attack = ["basic", "defense", "special"]):
    #returns error code if attack is invalid attack name
    if attack not in ("basic", "defense","special", "arrow", "elixer"): return 0
    #monsters don't have these special moves...
    if isinstance(attacker, (Chuchu, Bokoblin, Moblin, Darknut)) and attack in ("arrow", "elixer"): return 0
    #these are special moves only the player can use.
    if isinstance(attacker, Hero): 
        #setting actors tuple ensures that user prompt has correct grammer
        actors = ("you","opponent")
        if attack not in ("basic", "defense","special"): return special_hero_move(attacker, defender, attack)
    else: actors = ("opponent","you")
    eval("attacker.{}_attack(defender)".format(attack))
    print("{} used {}".format(actors[0], eval("attacker.{}_name()".format(attack))))
    print("{} : {} health points remaining".format(actors[1], defender.get_health()))
    return 1

def player_move(link, enemy):
    moves = {
    1 : '1) use master sword',
    2 : '2) use shield to block enemy attack',
    3 : '3) throw a bomb',
    4 : '4) shoot an arrow',
    5 : '5) drink an elixer',
    6 : '6) quit'}
    choices = {
    1 : 'basic',
    2 : 'defense',
    3 : "special",
    4 : "arrow",
    5 : "elixer",
    6 : "sys.exit(0)" }

    # # need input validation here

    while True:
        for i in range(1, 7): print(moves[i])
        choice = input("What would you like to do?\n")
        try:
            int(choice)
        except ValueError:
            print("Please provide a whole number. Try again.")
            continue
        if int(choice) not in range(1,7):
            print("Not a valid choice. Try again")
            continue
        elif choice == "help":
            continue
        elif choice in ('6','quit'): sys.exit(0)
        
        attack(link, enemy, choices[int(choice)])
        return 1
    # return choices[int(choice)]


def test():
    import Room
    link = create_player()
    enemy = Room.create_opponent()
    # attack(link, enemy, attack = "basic")
    # starting_health(link, enemy)
    # print(link.get_health())
    player_move(link, enemy)

def starting_health(link, monster):
    link.reset_health()
    monster.reset_health()


# def zelda_battle(link, monster):
#     '''
#     '''
#     # more than certain we can get rid of this line
#     # winner = ''

#     #Reset health
#     starting_health(link, monster)


#     print(monster.getName())
#     print(monster.getDesc())
#     #sets who goes first, second
#     attacker = link
#     defender = monster
#     loop = True
#     while loop:
#         user = input("avaiable moves are: (1)use master sword (2)Hide behind shield (3)throw a bomb(special move)\n(4)use an elixer(heals 50% health) (5)shoot arrow(limited supply: deals greater damage then other attacks)\n(6)Type quit at anytime to leave the game.")
#         #handles quitting. exits the function, which returns a message that is printed outside the function which then proceeds to break from main loop
#         if user == "quit".lower() or user == "(6)" or user == 6:
#             print("Game over.\nThanks for playing.")
#             sys.exit()
            
#         if int(attacker.getHealth()) <= 0:
#             winner = "{}".format(monster.getName())
#             loop = False
#         elif user == "(1)" or user == "1" or user == "use master sword".lower():
#             link.basic_Attack(monster)
#             print("you used {}".format(link.basic_Name()))
#             print("Your foe has",monster.getHealth(),"health points remaining")
#             print(link.getDesc(),"\n\n")
#         elif user == "(2)" or user == "2" or user == "Hide behind shield".lower() or user == "shield".lower():
#             link.defense_Attack(monster)
#             print("you used {}".format(link.defense_Name()))
#             print("Your foe has",monster.getHealth(),"health points remaining")
#             print(link.getDesc(),"\n\n")
#         elif user == "(3)" or user == "3".lower() or user == "throw a bomb".lower() or user == "special attack".lower():
#             link.special_Attack(monster)
#             print("you used {}".format(link.special_Attack(enemy)))
#             print("Your foe has",monster.getHealth(),"health points remaining")
#             print(link.getDesc(),"\n\n")
#         elif user == "(4)".lower() or user == "4".lower() or user == "use an elixer".lower() or user == "elixer".lower():
#             if int(link.elixer_Count()) < 1:
#                 print("You have run out of elixers")
#                 break
#             link.elixer()
#             print("you used {}".format(link.elixer()))
#             print(link.getDesc(),"\n\n")
#         elif user == "(5)".lower() or user == "5".lower() or user == "use an arrow".lower() or user == "arrow".lower():
#             if int(link.arrow_Count()) < 1:
#                 print("Your quiver is empty")
#                 break
#             link.use_Arrow(monster)
#             print("you used {}".format(link.arrow_Name()))
#             print("Your foe has",monster.getHealth(),"health points remaining")
#             print(link.getDesc(),"\n\n")
#         #monsters turn to attack: 1 out of 3 moves are randomly selected, then message about attack is printed out.
#         if int(defender.getHealth()) < 0:
#             print("you defeated this monster, Great work!")
#             winner = "{}".format(link.getName())
#             loop = False
#             break
#         chose = random.randint(1,3)
#         if chose == 1:
#             monster.basic_Attack(link)
#             print("your opponent used",monster.basic_Name())
#             print("Your health is now:",link.healthBar())
#         if chose == 2:
#             monster.defense_Attack(link)
#             print("your opponent used",monster.defense_Name())
#             print("Your health is now:",link.healthBar())
#         if chose == 3:
#             monster.special_Attack(link)
#             print("your opponent used",monster.special_Name())
#             print("Your health is now:",link.healthBar())
#     #handles returning the appropriate values
#     if winner == (link.getName()):
#         return winner
#     elif winner == (monster.getName()):
#         return winner
#     else:
#         return winner

# def extra_stuff():
#     '''
# main function takes no parameters, no return values
# handles running all program features
#     '''
#     random.seed(0)
#     if __name__=="__main__":
#         loop = True
#         while loop:
#             #loops continuosly until player decides to stop playing
#             for i in monster_list:
#                 winner = zelda_Battle(link, i)
#             if winner != "link":
#                 print("you were defeated. Better Luck next time.")
#                 loop = False
#             else:
#                 print("You have defeated all the available monsters.")
#                 choose = input("continue to search for markar (yes)/(no)? or look for more monsters to fight?")
#                 if choose == "yes".lower() or choose == "yeah".lower() or choose == "ye".lower():
#                     triforce()
#                     print("Good luck saving Makar. God Speed {}!!!".format(link.getName()))
#                     loop = False
#                 elif choose == "no":
#                     loop = True

# main()
test()