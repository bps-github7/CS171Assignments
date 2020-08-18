'''Module Level docstring:

'''

from CS171Assignments.Zelda_CLI_game.Enemies.Bokoblin import Bokoblin
from CS171Assignments.Zelda_CLI_game.Enemies.Chuchu import Chuchu
from CS171Assignments.Zelda_CLI_game.Enemies.Moblin import Moblin
from CS171Assignments.Zelda_CLI_game.Enemies.Darknut import Darknut
import random

def create_opponent():
    '''Creates a random monster with a random name'''
    monsters = ["Chuchu","Bokoblin","Moblin","Darknut"]
    names = ["Gary", "Fred", "Joyce", "Franklin", "Bruce", "Bstaltkja",
    "Tristeece", "Pinecone", "Frued", "Kongjawn", "Stanely", "Alfie",
    "John","Tommy","Arthur", "Mosely","Winston", "Aberama",
    "Tommy Carcetti", "Jon Bogotti", "Al Capone", "Michael Gray", "Polly Gray",
    "Skeleton Farce", "Strong wimsical Biscuit", "Spaggeti Monster",
    "QuasiHempt Skolondious", "Pastry Wimpleton", "Casey Busketon",
    "Railyway Eddie", "Eggplant Parmesean", "Ron Waffelmobile",
    "Cranberry Jones", "Spaulding Hernia", "Ernst Goatweight", "Golden Girl",
    "Sperta Mclewin", "Phife dawg", "Mohamamed Ali", "Spencer Goatpaste",
    "Flailing armdillo", "Purple space unit", "grey farm armadillo", "Mason faceplant"]
    return eval("{}('{}')".format(random.choice(monsters),random.choice(names)))


def get_reward():
    '''Decides if a room contains a reward. less than favoraable odds'''
    return 1 if random.random() < .2 else 0

def get_room_name():
    '''returns a random room name.
    Those prepended with * will end the game
    if dungeon.count > 10'''
    desc = random.choice([
    "enterance",
    "kitchen",
    "pancake-storage",
    "popsicle factory",
    "graveyard",
    "barn",
    "stable",
    "biege sportscoat club",
    "assylum",
    "weasel yard",
    "sports plaza",
    "zesty claptrap arena",
    "rap god's tenis court",
    "hedgehog dispensery",
    "plastic armadilo training facility",
    "sticky potato room",
    "flamingo land yaucht",
    "*purple dinosuar zone", 
    "*roman banana room",
    "*tall molerat bundle room",
    "*exit"])
    return desc.title()

def get_room_desc():
    return random.choice([
    "Pretzels litter the ground, the walls are yellow and brown,\n\
    \r\rsome sausages roll down the stairs near the walrus painting",
    "the room is filled with rabbits, too many to see clearly,\n\
    \r\rapricots hang from the cieling, and you pick a fresh one",
    "A gang of school children cheer for the monster, you smell toothpaste.\n\
    \r\rBarrels line the walls in the hallway near the exit",
    "A basset hound the size of the moon barks loudly, the ground trembles.\n\
    \r\rYou run quickly but are pulled aboard by the monsters. looking for a fight",
    "Weasels tear at the flesh of your face,  and thousands of microscopic\n\
    \r\rhorses race in subway tracks below your feet",
    "This average-sized, L-shaped bedroom has mismatched wooden furniture.\n\
    \r\rThe room is done in warm vivid colors and overall has a rustic look to it.",
    "This small chamber seems divided into three parts. The first has\n\
    \r\rseveral hooks on the walls from which hang dusty robes.\n\
    \r\rAn open curtain separates that space from the next,\n\
    \r\rwhich has a dry basin set in the floor.",
    "The scent of sweat and blood lingers, which makes the pit's \n\
    \r\rresemblance to a fighting pit or gladiatorial arena even stronger",
    "In the center of this large room lies a 30-foot-wide round pit,\n\
    \r\rits edges lined with rusting iron spikes. About 5 feet away from\n\
    \r\rthe pit's edge stand several stone semicircular benches",
    "The door to this room swings open easily on well-oiled hinges.\n\
    \r\rBeyond it you see that the chamber walls have been disguised\n\
    \r\rby wood paneling, and the stone ceiling and\n\
    \r\rfloor are hidden by bright marble tiles",
    "Several large and well-stuffed chairs are arranged about the room\n\
    \r\ralong with some small reading tables",
    "This room is a small antechamber before two titanic bronze doors.\n\
    \r\rEach stands 20 feet tall and is about 7 feet wide.\n\
    \r\rThe double doors are peaked at their centers,\n\
    \r\rbut unlike many sets of double doors,\n\
    \r\rtheir division isn't in the center",
    "This chamber served as an armory for some group of creatures.\n\
    \r\rArmor and weapon racks line the walls and\n\
    \r\rrusty and broken weapons litter the floor",
    "Several white marble busts that rest on white pillars\n\
    \r\rdominate this room. Most appear to be male or female humans\n\
    \r\rof middle age, but one clearly bears small horns projecting\n\
    \r\rfrom its forehead and another is spread across the floor in\n\
    \r\ra thousand pieces, leaving one pillar empty",
    "A stone throne stands on a foot-high circular dais in the center\n\
    \r\rof this cold chamber. The throne and dais bear the simple \n\
    \r\radornments of patterns of crossed lines",
    "There's a hiss as you open this door, and you smell a sour odor,\n\
    \r\rlike something rotten or fermented. Inside you see a small room\n\
    \r\rlined with dusty shelves, crates, and barrels. It looks like\n\
    \r\rsomeone once used this place as a larder,\n\
    \r\rbut it has been a long time since anyone came to retrieve food from it. ",
    "This chamber was clearly smaller at one time,\n\
    \r\rbut something knocked down the wall that separated it from an adjacent room",
    "Looking into this space, you see signs of another wall knocked over.\n\
    \r\rIt doesn't appear that anyone made an effort to clean up the rubble,\n\
    \r\rbut some paths through see more usage than others",
    "This small bare chamber holds nothing but a large ironbound chest,\n\
    \r\rwhich is big enough for a man to fit in and bears a heavy iron lock",
    "Unlike the flagstone common throughout the dungeon,\n\
    \r\rthis room is walled and floored with black marble veined with white.\n\
    \r\rThe ceiling is similarly marbled, but the thick pillars that\n\
    \r\rhold it up are white. A brown stain drips down one side of a nearby pillar",
    "You open the door to confront a room of odd pillars.\n\
    \r\rWater rushes down from several holes in the ceiling,\n\
    \r\rand each hole is roughly a foot wide",
    "Rusting spikes line the walls and ceiling of this chamber.\n\
    \r\rThe dusty floor shows no sign that the walls move over it,\n\
    \r\rbut you can see the skeleton of\n\
    \r\rsome humanoid impaled on some wall spikes nearby",
    "Thick cobwebs fill the corners of the room,\n\
    \r\rand wisps of webbing hang from the ceiling and\n\
    \r\rwaver in a wind you can barely feel.\n\n\
    \r\rOne corner of the ceiling has a particularly large clot\n\
    \r\rof webbing within which a Bokoblin's bones are tangled. ",
    "You open the door, and the reek of garbage assaults your nose.\n\
    \r\rLooking inside, you see a pile of refuse and offal that nearly reaches the ceiling",
    "Looking into this room, you note four pits in the floor.\n\
    \r\rA wide square is nearest you, a triangular pit beyond it,\n\
    \r\rand a little farther than both lie two circular pits",
    "Stinking smoke wafts up from braziers made of skulls set\n\
    \r\raround the edges of this room. The walls bear scratch marks\n\
    \r\rand lines of soot that form crude pictures and what looks like words in some language",
    "Neither light nor darkvision can penetrate the gloom in this chamber.\n\
    \r\rAn unnatural shade fills it, and the room's farthest reaches are barely visible",
    "You push open the stone door to this room and note that the only other exit\n\
    \r\ris a door made of wood. It and the table shoved against it are warped and swollen.\n\
    \r\rIndeed, the table only barely deserves that description",
    "This room looks like it was designed by drow. Rusted metal tiles create a huge mosaic\n\
    \r\rof a spider in the floor, and someone set up rusted gratings like draperies of webs.",
    "This chamber is clearly a prison. Small barred cells line the walls,\n\
    \r\rleaving a 15-foot-wide pathway for a guard to walk.",
    "The burble of water reaches your ears after you open the door to this room.\n\
    \r\rYou see the source of the noise in the far wall:\n\
    \r\ra large fountain artfully carved to look like a seashell\n\
    \r\rwith the figure of a seacat spewing clear water into its basin"
    ])

class Room:
    '''Class Docstring:
    
    '''
    def __init__(self):
        self.name = get_room_name()
        self.description = get_room_desc()
        self.enemy = create_opponent()
        self.reward = get_reward()
        self.north = self
        self.south = self
        self.east = self
        self.west = self

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

    @classmethod
    def from_repr(cls, arg):
        '''sort of unpythonic, but expected 
        use case is only within this class'''
        return Room(**arg)
