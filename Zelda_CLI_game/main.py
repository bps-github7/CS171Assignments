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
print(sys.path)
# from Dungeon.Maze import Maze
from Fighting import zelda_battle

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

def main():
    ''''''
    intro()
    triforce()
    Maze.create_maze()
    link = create_player()

def starting_health(link, monster):
    link.reset_health()
    monster.reset_health()

def check_health(link, monster):
    print("You: {} health points".format(link.get_health()))
    print("Opponent: {} health points".format(monster.get_health()))

def test():
    import Room
    ### remove the monotany of recreating player name every time
    # link = create_player()
    link = Hero("linko")
    enemy = Room.create_opponent()
    zelda_battle(link, enemy)

test()