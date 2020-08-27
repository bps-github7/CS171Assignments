'''Module Level Docstring: 
Programmer: Ben Sehnert
Program: Zelda Command line Mini-game
Date: 8/15/2020

'''
import time
import random
import sys
sys.path.insert(0, 'c:\\Users\\Ben\\VsCode\\CS171Assignments\\Zelda_CLI_game')
from Hero import Hero
sys.path.insert(0, 'c:\\Users\\Ben\\VsCode\\CS171Assignments\\Zelda_CLI_game\\Enemies')
from Enemies.Bokoblin import  Bokoblin
from Enemies.Chuchu import Chuchu
from Enemies.Moblin import Moblin
from Enemies.Darknut import Darknut
sys.path.insert(0, 'c:\\Users\\Ben\\VsCode\\CS171Assignments\\Zelda_CLI_game\\Dungeon')
from Dungeon.Maze import Maze

def game_over():
    '''prints game over- shown if user dies in battle'''
    print('''
          _             _                 _   _        _               _     _          _      _            _      
        /\ \          / /\              /\_\/\_\ _   /\ \            /\ \  /\ \    _ / /\    /\ \         /\ \    
       /  \ \        / /  \            / / / / //\_\/  \ \          /  \ \ \ \ \  /_/ / /   /  \ \       /  \ \   
      / /\ \_\      / / /\ \          /\ \/ \ \/ / / /\ \ \        / /\ \ \ \ \ \ \___\/   / /\ \ \     / /\ \ \  
     / / /\/_/     / / /\ \ \        /  \____\__/ / / /\ \_\      / / /\ \ \/ / /  \ \ \  / / /\ \_\   / / /\ \_\ 
    / / / ______  / / /  \ \ \      / /\/________/ /_/_ \/_/     / / /  \ \_\ \ \   \_\ \/ /_/_ \/_/  / / /_/ / / 
   / / / /\_____\/ / /___/ /\ \    / / /\/_// / / /____/\       / / /   / / /\ \ \  / / / /____/\    / / /__\/ /  
  / / /  \/____ / / /_____/ /\ \  / / /    / / / /\____\/      / / /   / / /  \ \ \/ / / /\____\/   / / /_____/   
 / / /_____/ / / /_________/\ \ \/ / /    / / / / /______     / / /___/ / /    \ \ \/ / / /______  / / /\ \ \     
/ / /______\/ / / /_       __\ \_\/_/    / / / / /_______\   / / /____\/ /      \ \  / / /_______\/ / /  \ \ \    
\/___________/\_\___\_    /____/_/       \/_/\/__________/   \/_________/ _      \_\/\/__________/\/_/    \_\/    
/\ \     /\_\       /\ \  /\_\                   /\ \         /\ \       /\ \      /\ \                           
\ \ \   / / /      /  \ \/ / /         _        /  \ \____    \ \ \     /  \ \    /  \ \____                      
 \ \ \_/ / /      / /\ \ \ \ \__      /\_\     / /\ \_____\   /\ \_\   / /\ \ \  / /\ \_____\                     
  \ \___/ /      / / /\ \ \ \___\    / / /    / / /\/___  /  / /\/_/  / / /\ \_\/ / /\/___  /                     
   \ \ \_/      / / /  \ \_\__  /   / / /    / / /   / / /  / / /    / /_/_ \/_/ / /   / / /                      
    \ \ \      / / /   / / / / /   / / /    / / /   / / /  / / /    / /____/\ / / /   / / /                       
     \ \ \    / / /   / / / / /   / / /    / / /   / / /  / / /    / /\____\// / /   / / /                        
      \ \ \  / / /___/ / / / /___/ / /     \ \ \__/ / /__/ / /__  / / /______\ \ \__/ / /                         
       \ \_\/ / /____\/ / / /____\/ /       \ \___\/ /\__\/_/___\/ / /_______\\ \___\/ /                          
        \/_/\/_________/\/_________/         \/_____/\/_________/\/__________/ \/_____/                           
                                                                                        ''')

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

def bomb(attacker, defender):
    print("{} used {}".format(attacker.get_name(), attacker.special_name()))
    print(attacker.special_attack(defender))
    return 1

def special_hero_move(attacker, defender, attack):
    if attack == "elixer":
        return elixer(attacker)
    elif attack == "arrow":
        return arrow(attacker, defender)
    else:
        bomb(attacker, defender)

def attack(attacker, defender, attack = ["basic", "defense", "special"]):
    #returns error code if attack is invalid attack name
    if attack not in ("basic", "defense","special", "arrow", "elixer"): return 0
    #monsters don't have these special moves...
    if isinstance(attacker, (Chuchu, Bokoblin, Moblin, Darknut)) and attack in ("arrow", "elixer"): return 0
    #these are special moves only the player can use.
    if isinstance(attacker, Hero): 
        #setting actors tuple ensures that user prompt has correct grammer
        actors = ("you","opponent")
        if attack not in ("basic", "defense"): return special_hero_move(attacker, defender, attack)
    #not sure if u need this actors thing since moving health bar display out of here...
    else: actors = ("opponent","you")
    eval("attacker.{}_attack(defender)".format(attack))
    print("{} used {}".format(actors[0], eval("attacker.{}_name()".format(attack))))
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
    validate(link, enemy, choices, moves)
    # choice = validate(moves)
    # if choice:
    #     return attack(link, enemy, choices[int(choice)])
    
def validate(link, enemy, choices, moves):
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
        return attack(link, enemy, attack = choices[int(choice)])



def starting_health(link, monster):
    link.reset_health()
    monster.reset_health()

def check_health(link, monster):
    print("You: {} health points".format(link.get_health()))
    print("Opponent: {} health points".format(monster.get_health()))

def monster_move(link, monster):
    '''picks a move from a set of 3
    invokes it on link and prints feedback to user.'''
    return attack(monster, link, attack = random.choice(["basic","defense","special"]))

def player_turn(link, monster):
    player_move(link, monster)
    if monster.get_health(numeric = True) <= 0:
        print("you defeated {}".format(monster.get_name()))
        print("good work.")
        return True
    print("opponent: {} Health points remaining".format(monster.get_health()))

def monster_turn(link, monster):
    monster_move(link, monster)
    if link.get_health(numeric = True) <= 0:
        game_over()
        print("You were defeated. Better luck next time!")
        return False
    print("you: {} health points remaining".format(link.get_health()))

def zelda_battle(link, monster):
    # reset both opponents health
    # # suspect there is a neater way to do this via tuple unpacking...
    starting_health(link, monster)
    # print(link.get_health())
    #itd be cool if this condition worked. but it doesnt look like it will
    while ((link.get_health(numeric = True) > 0) and (monster.get_health(numeric = True) > 0)):
        winner = player_turn(link, monster)
        if winner: return True
        monster_turn(link, monster)
        
        

def test():
    import Room
    ### remove the monotany of recreating player name every time
    # link = create_player()
    link = Hero("linko")
    enemy = Room.create_opponent()
    zelda_battle(link, enemy)

test()