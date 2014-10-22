from items import *
from enemies import *

place_village = {
    "name": "Village",

    "description":
    """Ahead of you is a small village that you are able to enter. To the North lies a vast arena. To the east lies some sinister looking caves.
    There is a large green lake to the south, and a large dark forest lies to the west.""",

    "exits": {"north": "Arena", "east": "Caves", "south": "Lake", "west": "Forest", "enter": "Shops"},

    "items": [],

    "battle": False
}

place_forest = {
    "name": "The Spooky Forest",

    "description":
    """The dark forest is cold and the thick fog acts as a blanket across the mossy landscape. The ground beneath your feet is waterlogged and squishy.
    Strange noises can be heard in the distance, the bushes russell behind you, when you turn round there is nothing there.
    A small stream trickles down the valley towards the south.
    Toward the north the forest starts to thicken as sunlight is almost completely lost amongst the trees,
    more strange noises can be heard deeper into the forest""",

    "exits":  {"west": "Village", "north": "Deeper", "south": "Stream"},

    "items": [],

    "battle": True
}

place_deeper = {
    "name": "Deep Forest",

    "description":
    """The darkness of the forest limits your vision. The tree’s block the sunlight from above and a cold chill runs down your spine.
    The strange noises that you heard before are getting louder the deeper you walk.""",

    "exits": {"south": "Forest"},

    "items": [],

    "battle": True
}

place_stream = {
    "name": "Forest Stream",

    "description":
    """A small quiet clearing is surrounded by some tall trees rustling in the wind, a stream trickles quietly along the ground.
    There are noises coming from the dark areas underneath the trees.
    The clearing is a dead end, you can only go north back to the forest.""",

    "exits": {"north": "Forest"},

    "items": [],

    "battle": True
}

place_knight = {
    "name": "Knight's Cave",

    "description":
    """Following the winding burnt stone walls of the cave you come to an opening with large bones scattered across the floor.
    The bones look human. Looking deeper into the opening there is a large dragon skeleton in the centre of the cave.
    Upon closer inspection of the skeleton you find a fallen knight in full royal armour.
    The knight climbs to his feet and draws his sword.""",

    "exits": {"west": "Caves"},

    "items": [],

    "battle": False
}

place_goblin = {
    "name": "Goblin's Cave",

    "description":
    """You have crept into an opening deep in the cave which is lit by multiple torches across the walls of the cave.
    You can make out creature like shadows on the walls from the opening of the cave.
    Whilst you try and creep closer your sword drops and makes a large clanging noise on the floor, you scatter frantically to pick it up.
    You look up from the cave floor to find a large goblin standing in front of you bearing a sharp pointed spear.
    He looks ready to fight and you squeeze your weapon ready""",

    "exits": {"south": "Caves"},

    "items": [],

    "battle": False
}

place_gutfeel = {
    "name": "Gut Feeling",

    "description":
    """Your gut feeling is starting to feel a little bit off. As you walk deeper and deeper into the cave it gets even more dark.
    You are now in complete darkness.
    You should probably go back to to the main entrance but as soon as you turn round
    a shadowed figure hits you across the head, knocking you unconscious.""",

    "exits": {"north": "Caves"},

    "items": [],

    "battle": False
}

place_caves = {
    "name": "Forbidden Caves",

    "description":
    """The cave entrance is littered with bones of animals, the stench of death is strong in the air.
    As you walk carefully into the cave entrance your eyes adjust to the darkness. The path is split into three.
    There are noises of strange conversations coming from the northern exit, whatever is talking doesnt sound human.
    The walls of the western exit look blackened as if they have been burnt. The southern path leads to a dark deeper cave,
    but your gut feeling tells you that there is something of interest down there.""",

    "exits": {"west": "Village", "east": "Knight", "north": "Goblin", "south": "Gut Feeling"},

    "items": [],

    "battle": True
}

place_lake = {
    "name": "The Green Lake",

    "description":
    """As you walk down the slippery banks toward the murky lake you notice that the water is not completely still.
    Small bubbles rise and then pop on the surface of the murky green water.
    As you descend the muddy banks of the lake your foot dislodges a stone and it falls into the lake.
    To the south stands a small separate part of the lake, a sign with the words “Beware the beast” hangs loosely on a rock.""",

    "exits": {"north": "Village", "south": "Lair"},

    "items": [],

    "battle": True
}

place_shops = {
    "name": "Town Center",

    "description":
    """The hustle and bustle of village life moves quickly around you. The cobblestone path beneath you leads to the village square.
    Which has an ornate sculpted fountain at the center with children playing games beside it.
    Stalls selling goods and fine foods are spread amongst the crowds of people bartering for the best deals.
    The stone houses surrounding the square look tired and withered, some of  the thatched roofs are crumbling.
    Many a strange person can be seen amongst the crowds, an armorsmith is loudly hammering away at a steel chest piece towards the east.
    A shop at the far southern end of the square has weapons displayed in its windows, to the north there is a training ground for knights and warriors alike,
    where groups of men are sparring.
    Your small home sits quaintly at the west side of the village.""",

    "exits": {"north": "Gym", "east": "Armour", "south": "Weapons","west": "Home", "exit": "Village"},

    "items": [],

    "battle": False
}

place_arena = {
    "name": "Arena",

    "description": """As you approach the loud grounds of the arena you are met by two paths.
    The path leading towards the east marked arena has deafening amounts of cheering and people are rushing towards the circular fighting grounds.
    A booth at the foot of the path is marked ‘FIGHTERS WANTED BIG REWARD’.
    The path to the west leads towards a huge marble wall with rows upon rows of names chiseled into it, it is titled ‘Hall Of Fame'.""",

    "exits": {"south": "Village", "west": "Battle", "east": "Leaderboards"},

    "items": [],

    "battle": False
}

place_leaderboard = {
    "name": "Leaderboard",

    "description":
    """This giant marble wall has rows upon rows of fallen warriors etched upon the marble.""",

    "exits": {"east": "Arena"},

    "items": [],

    "battle": False
}

place_battle = {
    "name": "Battlefield",

    "description":
    """The deafening noise of cheering onlookers spreads throughout the north. The arena walls are high and crowds start to flood into the fastly filling stands.
    The King sits high above the crowds in his own personal box, the Queen by his side. As you walk through the dark tunnel leading to the main arena you notice
    the sand is stained with blood of fallen heroes. Your opponents walk in at the opposite side of the arena and you meet them in the middle along with the
    arena enforcers. The crowd silences as the King stands to speak.
    After which you stare down your opponent before the fight begins.""",

    "exits": {"east": "Arena"},

    "items": [],

    "battle": False
}

place_gym = {
    "name": "Gym",

    "description":
    """The noise of angry men wrestling is met by the clang of swords clashing in the air. The sign reads above the fighting quarters “THE GYM.""",

    "exits": {"south": "Shops"},

    "items": [],

    "battle": False
}

place_weapons = {
    "name": "Weapons",

    "description":
    """As you enter the weaponsmith’s shop you are stunned by the sheer amount of shiny weaponry there is on offer. ‘Hello friend!’
    the weaponsmith shouts from behind the counter,
    ‘And what is it i can do for you on this fine day?’. You approach the fat bearded man.""",

    "exits": {"north": "Shops"},

    "items": [weapon_dagger, weapon_sword, weapon_2hand],

    "battle": False
}

place_armour = {
    "name": "Armour",

    "description":
    """The big burly armoursmith ignores you as you first walk in and continues to hammer away at a large steel sword.
    You are amazed at the intricate armour displays that are on display. “What do you want?” the scarred armoursmith says.""",

    "exits": {"west": "Shops"},

    "items": [armour_halfhelm, armour_chain, armour_plate],

    "battle": False
}

place_home = {
    "name": "Home",

    "description":
    """This is you warm humble home. The fire is burning brightly in the corner, with your shaggy coat sheep dog lying asleep besides it.""",

    "exits": {"east": "Shops"},

    "items": [],

    "battle": False
}

place_lair = {
    "name": "Kraken Lair",

    "description":
    """Time to fight, prepare to die or have your name live on through history.""",

    "exits": {},

    "items": [],

    "battle": False
}

places = {
    "Home": place_home,
    "Armour": place_armour,
    "Village": place_village,
    "Forest": place_forest,
    "Gym": place_gym,
    "Shops": place_shops,
    "Arena": place_arena,
    "Leaderboard": place_leaderboard,
    "Battle": place_battle,
    "Weapons": place_weapons,
    "Caves": place_caves,
    "Stream": place_stream,
    "Deeper": place_deeper,
    "Lake": place_lake,
    "Lair": place_lair
    "Gut": place_gutfeel
    "Knight": place_knight
    "Goblin": place_goblin
}
