###Ben Sehnert
###8.16.18
###CS172 HW3 battle simulation

#Modules Imported
import time
import random
import sys
#classes imported
from Hero import *
from Bokoblin import *
from Chuchu import *
from Darknut import *
from Moblin import *
#start screen
print(r'''                                       /@
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
           \=\  /________________|/=/    
             \==\     _____     /==/ 
            / \===\   \   /   /===/
           / / /\===\  \_/  /===/
          / / /   \====\ /====/
         / / /      \===|===/
         |/_/         \===/
                        = ''')
print("{:=^98s}".format("Welcome to Legend of Zelda: Python Edition"))#welcome screen

#first user prompt
name = "link";
name = input("Enter your name(default = Link): ")

#defaults player name to link if nothing is inputted
if name == "":
    link = Hero("link")
else:
    link = Hero(name)

#intro 
time.sleep(1.4)
print("You are exploring deep in a dark forbidden woods,\nSent by the Greak Deku tree to rescue a Korok called Makar...\n\n")
time.sleep(1.2)
print("out of nearby bushes you hear a shufflin of brushes'\n\n")
time.sleep(1.2)

#initializes user input section: asks user how many mosters they want to fight. restriction on selection greater than 5, in order to make coding this practical
loop = True;
while loop:
    count = input("You look closely and realize it be monsters.\nHow many do you wish to fight?\n\n")
    try:
        count = int(count)
        if int(count) > 5:
            print("That sure is a lot of monsters.\nYou will fight five monsters and then decide if you want to keep going.")
        loop = False;
    except ValueError:
        print("there is no such thing as a",count,"quantity of monsters!\nTry again.\n\n\n")

#Randomly populates monster_list with selection of monsters named after rappers and etc characters

#Gotta be a better way of using the constructors (ie use random name from array and unpack arg) than this!!!

monster_list = []
if count == 1:
    ran = random.randint(1,3)
    if ran == 1:
        monster1 = Chuchu('Blue')
        monster_list.append(monster1)
        count -= 1;
    elif ran == 2:
        monster1 = Bokoblin('Gary')
        monster_list.append(monster1)
        count -= 1;
    elif ran == 3:
        monster1 = Moblin("Moe")
        monster_list.append(monster1)
elif count == 2:
    ran = random.randint(1,3)#would have used a for loop if i could have figured out how to make that work
    if ran == 1:#for now, this works
        monster1 = Darknut("Mayor Nutter")
        monster_list.append(monster1)
        monster2 = Chuchu("Blob")
        monster_list.append(monster2)
        count -= 1;
    if ran == 2:
        monster1 = Bokoblin("Todd")
        monster_list.append(monster1)
        monster2 = Darknut("Dr. Storm")
        monster_list.append(monster2)
    if ran == 3:
        monster1 = Moblin("Mos Def")
        monster_list.append(monster1)
        monster2 = Bokoblin("Toothhead")
        monster_list.append(monster2)
elif count == 3:
    ran = random.randint(1,3)
    if ran == 1:
        monster1 = Chuchu("Gert")
        monster_list.append(monster1)
        monster2 = Darknut("Helen")
        monster_list.append(monster2)
        monster3 = Moblin("QTip")
        monster_list.append(monster3)
    if ran == 2:
        monster3 = Bokoblin("Jerobi")
        monster_list.append(monster3)
        monster2 = Bokoblin("Sir Greenthumb")
        monster_list.append(monster2)
        monster1 = Bokoblin("Eskimo Steve")
        monster_list.append(monster1)
    if ran == 3:
        monster1 = Chuchu("Ali Shaheed Mohhamed")
        monster_list.append(monster1)
        monster2 = Chuchu("Dakan Maban")
        monster_list.append(monster2)
        monster3 = Chuchu("Estiban Mobile")
        monster_list.append(monster3)
elif count == 4:
    ran = random.randint(1,3)
    if ran == 1:
        monster1 = Chuchu("Purple")
        monster_list.append(monster1)
        monster2 = Chuchu("Orangey")
        monster_list.append(monster2)
        monster3 = Chuchu("Lauren")
        monster_list.append(monster3)
        monster4 = Chuchu("Jackson Torez")
        monster_list.append(monster4)
        count -= 1;
    if ran == 2:
        monster1 = Darknut("Madiq")
        monster_list.append(monster1)
        monster2 = Darknut("Mopez")
        monster_list.append(monster2)
        monster3 = Darknut("Microagression")
        monster_list.append(monster3)
        monster4 = Darknut("Jope")
        monster_list.append(monster4)
    if ran == 3:
        monster1 = Moblin("Tyrone A")
        monster_list.append(monster1)
        monster2 = Moblin("Tyrone B")
        monster_list.append(monster2)
        monster3 = Moblin("Tyrone C")
        monster_list.append(monster3)
        monster4 = Moblin("Tyrone D")
        monster_list.append(monster4)
elif count == 5:
    ran = random.randint(1,3)
    if ran == 1:
        monster1 = Chuchu("Cream Boi")
        monster_list.append(monster1)
        monster2 = Chuchu("Ice Boi")
        monster_list.append(monster2)
        monster3 = Chuchu("Steam Boi")
        monster_list.append(monster3)
        monster4 = Chuchu("Milk Boi")
        monster_list.append(monster4)
        monster5 = Chuchu("Cone Boi")
        monster_list.append(monster5)
    if ran == 2:
        monster1 = Chuchu("PineSol Boi")
        monster_list.append(monster1)
        monster2 = Bokoblin("Apricot")
        monster_list.append(monster2);
        monster3 = Chuchu("Smolt")
        monster_list.append(monster3)
        monster4 = Chuchu("Piper")
        monster_list.append(monster4)
        monster5 = Bokoblin("Stan the Man from Afgahnistan")
        monster_list.append(monster5)
    if ran == 3:
        monster1 = Chuchu("Tinky-Winky")
        monster_list.append(monster1)
        monster2 = Moblin("Nose fan")
        monster_list.append(monster2);
        monster3 = Bokoblin("Scent boi")
        monster_list.append(monster3)
        monster4 = Chuchu("Elbow noodle")
        monster_list.append(monster4)
        monster5 = Darknut("Preston")
        monster_list.append(monster5)

def zelda_Battle(link, monster):
    """
Battle function facilitates battle between hero character and monsters
takes hero object and monster object as parameters
returns the winner
    """
    #problem variable set to empty string: refrenced before assignment error
    winner = ''
    
    #Reset health
    link.resetHealth()
    monster.resetHealth()

    print(monster.getName())
    print(monster.getDesc())
    #sets who goes first, second
    attacker = link;
    defender = monster;
    loop = True;
    while loop:
        user = input("avaiable moves are: (1)use master sword (2)Hide behind shield (3)throw a bomb(special move)\n(4)use an elixer(heals 50% health) (5)shoot arrow(limited supply: deals greater damage then other attacks)\n(6)Type quit at anytime to leave the game.")
        #handles quitting. exits the function, which returns a message that is printed outside the function which then proceeds to break from main loop
        if user == "quit".lower() or user == "(6)" or user == 6:
            print("Game over.\nThanks for playing.")
            sys.exit()#this does not work for some reason, it makes the computer throw an exception. Kimberlee told me the TA grading would not take points off, because the function isnt working the way its supposed to.
        #handles use of the 5 different moves: if elif else branches for move selection
        #appropriate object method is acted upon, then message is printed out about monster, hero health and inventory
        #if nessecary, if branch is used to notify users they have ran out of decremented items like elixer(potion) and arrow(fireball)    
        if int(attacker.getHealth()) <= 0:
            winner = "{}".format(monster.getName())
            loop = False
        elif user == "(1)" or user == "1" or user == "use master sword".lower():
            link.basic_Attack(monster);
            print("you used {}".format(link.basic_Name()))
            print("Your foe has",monster.getHealth(),"health points remaining");
            print(link.getDesc(),"\n\n")
        elif user == "(2)" or user == "2" or user == "Hide behind shield".lower() or user == "shield".lower():
            link.defense_Attack(monster);
            print("you used {}".format(link.defense_Name()))
            print("Your foe has",monster.getHealth(),"health points remaining");
            print(link.getDesc(),"\n\n")
        elif user == "(3)" or user == "3".lower() or user == "throw a bomb".lower() or user == "special attack".lower():
            link.special_Attack(monster);
            print("you used {}".format(link.special_Attack(enemy)))
            print("Your foe has",monster.getHealth(),"health points remaining");
            print(link.getDesc(),"\n\n")
        elif user == "(4)".lower() or user == "4".lower() or user == "use an elixer".lower() or user == "elixer".lower():
            if int(link.elixer_Count()) < 1:
                print("You have run out of elixers");
                break
            link.elixer();
            print("you used {}".format(link.elixer()))
            print(link.getDesc(),"\n\n")
        elif user == "(5)".lower() or user == "5".lower() or user == "use an arrow".lower() or user == "arrow".lower():
            if int(link.arrow_Count()) < 1:
                print("Your quiver is empty")
                break
            link.use_Arrow(monster);
            print("you used {}".format(link.arrow_Name()))
            print("Your foe has",monster.getHealth(),"health points remaining");
            print(link.getDesc(),"\n\n")
        #monsters turn to attack: 1 out of 3 moves are randomly selected, then message about attack is printed out.
        if int(defender.getHealth()) < 0:
            print("you defeated this monster, Great work!")
            winner = "{}".format(link.getName())
            loop = False;
            break
        chose = random.randint(1,3)
        if chose == 1:
            monster.basic_Attack(link);
            print("your opponent used",monster.basic_Name());
            print("Your health is now:",link.healthBar());
        if chose == 2:
            monster.defense_Attack(link);
            print("your opponent used",monster.defense_Name());
            print("Your health is now:",link.healthBar());
        if chose == 3:
            monster.special_Attack(link);
            print("your opponent used",monster.special_Name());
            print("Your health is now:",link.healthBar());
        
    
    #handles returning the appropriate values
    if winner == (link.getName()):
        return winner;
    elif winner == (monster.getName()):
        return winner;
    else:
        return winner
#----------------------------------------------------
#
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
def main():
    '''
main function takes no parameters, no return values
handles running all program features
    '''
    random.seed(0)
    if __name__=="__main__":
        loop = True;
        while loop:
            #loops continuosly until player decides to stop playing
            for i in monster_list:
                winner = zelda_Battle(link, i)
            if winner != "link":
                print("you were defeated. Better Luck next time.")
                loop = False;
            else:
                print("You have defeated all the available monsters.")
                choose = input("continue to search for markar (yes)/(no)? or look for more monsters to fight?")
                if choose == "yes".lower() or choose == "yeah".lower() or choose == "ye".lower():
                    triforce()
                    print("Good luck saving Makar. God Speed {}!!!".format(link.getName()));
                    loop = False
                elif choose == "no":
                    loop = True;
main()#intializes main function
