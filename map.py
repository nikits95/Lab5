from items import *
from enemies import *

place_village = {
    "name": "Village Gates",

    "description":
    """A small town situated in the country of Azgorth. Home to mighty warriors and 
the surrounded by vicious creatures, thirsty for blood.""",

    "exits": {"north": "Forest", "west": "Arena", "enter": "Shops"},

    "items": [],

    "battle": False
}

place_forest = {
    "name": "The Forest",

    "description":
    """The spooky Forest, containing evil men and demons and shit.""",

    "exits":  {"south": "Village", "north": "Deeper", "east": "Water", "west": "Caves"},

    "items": [],

    "battle": True
}

place_deeper = {
    "name": "Deep Forest",

    "description":
    """A place of enteral night where only the deadliest of monsters travel.""",

    "exits": {"south": "Forest"},

    "items": [],

    "battle": True
}

place_water = {
    "name": "Forest Stream",

    "description":
    """A small stream trickling through the Forest, most likely attracting animals.""",

    "exits": {"west": "Forest"},

    "items": [],

    "battle": True
}

place_caves = {
    "name": "Mountain Caves",

    "description":
    """A series of caves twisting deep into the face of a mountain, home to who knows what creatures.""",

    "exits": {"east": "Forest"},

    "items": [],

    "battle": True
}

place_shops = {
    "name": "Town Center",

    "description":
    """The town center containing all the shops.""",

    "exits": {"exit": "Village", "north": "Armour", "east": "Gym", "south": "Weapons", "west": "Home"},

    "items": [],

    "battle": False
}

place_arena = {
    "name": "Arena",

    "description": """The place to prove your worth and reflect on the best.""",

    "exits": {"east": "Village", "south": "Battle", "north": "Legends"},

    "items": [],

    "battle": False
}

place_legends = {
    "name": "Hall of Legends",

    "description":
    """The place to look at the record books.""",

    "exits": {"south": "Arena"},

    "items": [],

    "battle": False
}

place_battle = {
    "name": "Battle Field",

    "description":
    """The place to fight warriors.""",

    "exits": {"north": "Arena"},

    "items": [],

    "battle": False
}

place_gym = {
    "name": "Gym",

    "description":
    """The place to get buff.""",

    "exits": {"west": "Shops"},

    "items": [],

    "battle": False
}

place_weapons = {
    "name": "Weapons",

    "description":
    """The place to get weapons.""",

    "exits": {"north": "Shops"},

    "items": [weapon_dagger, weapon_sword, weapon_2hand],

    "battle": False
}

place_armour = {
    "name": "Armour",

    "description":
    """The place to get armour.""",

    "exits": {"south": "Shops"},

    "items": [armour_halfhelm, armour_chain, armour_plate],

    "battle": False
}

place_home = {
    "name": "Home",

    "description":
    """The place you live, obviously.""",

    "exits": {"east": "Shops"},

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
    "Legends": place_legends,
    "Battle": place_battle,
    "Weapons": place_weapons,
    "Caves": place_caves,
    "Water": place_water,
    "Deeper": place_deeper
}
