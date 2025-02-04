from enum import *
from Helper import *

# =================================
# ===         POTIONS           ===
# =================================

class Potions(Enum):
    T2_POTION_ENERGY = 474  # Minor Energy Potion
    T2_POTION_HEAL = 469  # Minor Healing Potion
    T3_POTION_REVIVE = 479  # Minor Gigantify Potion
    T3_POTION_STONESKIN = 484  # Minor Resistance Potion
    T3_POTION_ACID = 623 # Minor Acid Potion
    T3_POTION_MOB_RESET = 599 # Minor Calming Potion
    T3_POTION_CLEANSE2 = 611 # Minor Cleansing Potion
    T3_POTION_SLOWFIELD = 489  # Minor Sticky Potion
    T4_POTION_COOLDOWN = 494  # Minor Poison Potion
    T4_POTION_BERSERK = 635 # Minor Berserk Potion
    T4_POTION_LAVA = 647 # Minor Hellfire Potion
    T4_POTION_GATHER = 659 # Minor Gathering Potion
    T4_POTION_TORNADO = 671 # Minor Tornado in a Bottle

    T4_POTION_HEAL = 470  # Healing Potion
    T4_POTION_ENERGY = 475  # Energy Potion
    T5_POTION_SLOWFIELD = 490  # Sticky Potion
    T5_POTION_REVIVE = 480  # Gigantify Potion
    T5_POTION_STONESKIN = 485  # Resistance Potion
    T5_POTION_MOB_RESET = 603 # Calming Potion
    T5_POTION_CLEANSE2 = 615 # Cleansing Potion
    T5_POTION_ACID = 627 # Acid Potion
    T6_POTION_COOLDOWN = 496  # Poison Potion
    T6_POTION_BERSERK = 639 # Berserk Potion
    T6_POTION_LAVA = 651 # Hellfire Potion
    T6_POTION_GATHER = 663 # Gathering Potion
    T6_POTION_TORNADO = 675 # Tornado in a Bottle

    T6_POTION_HEAL = 472  # Major Healing Potion
    T6_POTION_ENERGY = 477  # Major Energy Potion
    T7_POTION_MOB_RESET = 607 # Major Calming Potion
    T7_POTION_REVIVE = 482  # Major Gigantify Potion
    T7_POTION_STONESKIN = 487  # Major Resistance Potion
    T7_POTION_SLOWFIELD = 492  # Major Sticky Potion
    T7_POTION_CLEANSE2 = 619 # Major Cleansing Potion
    T7_POTION_ACID = 631 # Major Acid Potion
    T8_POTION_COOLDOWN = 498  # Major Poison Potion
    T8_POTION_CLEANSE = 500  # Invisibility Potion
    T8_POTION_BERSERK = 643 # Major Berserk Potion
    T8_POTION_LAVA = 655 # Major Hellfire Potion
    T8_POTION_GATHER = 667 # Major Gathering Potion
    T8_POTION_TORNADO = 679 # Major Tornado in a Bottle

class BasicPotions(Enum):
    T2_POTION_ENERGY = 474  # Minor Energy Potion
    T2_POTION_HEAL = 469  # Minor Healing Potion
    T3_POTION_REVIVE = 479  # Minor Gigantify Potion
    T3_POTION_STONESKIN = 484  # Minor Resistance Potion
    T3_POTION_SLOWFIELD = 489  # Minor Sticky Potion
    T4_POTION_COOLDOWN = 494  # Minor Poison Potion

    T4_POTION_HEAL = 470  # Healing Potion
    T4_POTION_ENERGY = 475  # Energy Potion
    T5_POTION_SLOWFIELD = 490  # Sticky Potion
    T5_POTION_REVIVE = 480  # Gigantify Potion
    T5_POTION_STONESKIN = 485  # Resistance Potion
    T6_POTION_COOLDOWN = 496  # Poison Potion

    T6_POTION_HEAL = 472  # Major Healing Potion
    T6_POTION_ENERGY = 477  # Major Energy Potion
    T7_POTION_REVIVE = 482  # Major Gigantify Potion
    T7_POTION_STONESKIN = 487  # Major Resistance Potion
    T7_POTION_SLOWFIELD = 492  # Major Sticky Potion
    T8_POTION_COOLDOWN = 498  # Major Poison Potion
    T8_POTION_CLEANSE = 500  # Invisibility Potion

class BigFive(Enum):
    T6_POTION_HEAL = 472  # Major Healing Potion
    T6_POTION_ENERGY = 477  # Major Energy Potion
    T7_POTION_REVIVE = 482  # Major Gigantify Potion
    T7_POTION_STONESKIN = 487  # Major Resistance Potion
    T8_POTION_COOLDOWN = 498  # Major Poison Potion
    T8_POTION_CLEANSE = 500  # Invisibility Potion

pots = Potions

# Dictionary mapping potion constants to potion names
potion_dict = {
    "T2_POTION_ENERGY": "Minor Energy Potion",
    "T2_POTION_HEAL": "Minor Healing Potion",
    "T3_POTION_ACID": "Minor Acid Potion",
    "T3_POTION_CLEANSE2": "Minor Cleansing Potion",
    "T3_POTION_MOB_RESET": "Minor Calming Potion",
    "T3_POTION_REVIVE": "Minor Gigantify Potion",
    "T3_POTION_SLOWFIELD": "Minor Sticky Potion",
    "T3_POTION_STONESKIN": "Minor Resistance Potion",
    "T4_POTION_BERSERK": "Minor Berserk Potion",
    "T4_POTION_COOLDOWN": "Minor Poison Potion",
    "T4_POTION_GATHER": "Minor Gathering Potion",
    "T4_POTION_LAVA": "Minor Hellfire Potion",
    "T4_POTION_TORNADO": "Minor Tornado In A Bottle",

    "T4_POTION_ENERGY": "Energy Potion",
    "T4_POTION_HEAL": "Healing Potion",
    "T5_POTION_ACID": "Acid Potion",
    "T5_POTION_CLEANSE2": "Cleansing Potion",
    "T5_POTION_MOB_RESET": "Calming Potion",
    "T5_POTION_REVIVE": "Gigantify Potion",
    "T5_POTION_SLOWFIELD": "Sticky Potion",
    "T5_POTION_STONESKIN": "Resistance Potion",
    "T6_POTION_BERSERK": "Berserk Potion",
    "T6_POTION_COOLDOWN": "Poison Potion",
    "T6_POTION_GATHER": "Gathering Potion",
    "T6_POTION_LAVA": "Hellfire Potion",
    "T6_POTION_TORNADO": "Tornado In A Bottle",

    "T6_POTION_ENERGY": "Major Energy Potion",
    "T6_POTION_HEAL": "Major Healing Potion",
    "T7_POTION_ACID": "Major Acid Potion",
    "T7_POTION_CLEANSE2": "Major Cleansing Potion",
    "T7_POTION_MOB_RESET": "Major Calming Potion",
    "T7_POTION_REVIVE": "Major Gigantify Potion",
    "T7_POTION_SLOWFIELD": "Major Sticky Potion",
    "T7_POTION_STONESKIN": "Major Resistance Potion",
    "T8_POTION_BERSERK": "Major Berserk Potion",
    "T8_POTION_COOLDOWN": "Major Poison Potion",
    "T8_POTION_GATHER": "Major Gathering Potion",
    "T8_POTION_LAVA": "Major Hellfire Potion",
    "T8_POTION_TORNADO": "Major Tornado In A Bottle",
    "T8_POTION_CLEANSE": "Invisibility Potion"
}

potion_weight_dict = {
    BigFive.T6_POTION_HEAL: 0.9,
    BigFive.T6_POTION_ENERGY: 0.9,
    BigFive.T7_POTION_REVIVE: 1.2,
    BigFive.T7_POTION_STONESKIN: 1.4,
    BigFive.T8_POTION_COOLDOWN: 1.4,
    BigFive.T8_POTION_CLEANSE: 1.4
}

# Function to get potion name from potion constant
def get_potion_name(potion_constant):
    return potion_dict.get(potion_constant, POT_NAME_NOT_FOUND_ERR)

def get_potions_array():
    POTS = []
    for p in pots:
        POTS.append(p.name)
    return POTS

def get_big_pots_array():
    POTS = []
    for p in BigFive:
        POTS.append(p.name)
    return POTS

def get_potions_name_array():
    POTS = []
    for p in pots:
        POTS.append(get_potion_name(p.name))
    return POTS

def get_potions_string():
    return ','.join(potion.name for potion in pots)

def get_tier_from_potid(potion_id_string):
    return potion_id_string.split('_')[0][1:]

# =================================
# ===        INGREDIENTS        ===
# =================================

class Ingredients(Enum):
    T2_AGARIC = 126  # Arcane Agaric
    T3_COMFREY = 127 # Brightleaf Comfrey
    T8_BUTTER = 901 # Cow's Butter
    T8_MILK = 137 # Cow's Milk
    T7_CORN = 124 # Bundle of Corn
    T4_BURDOCK = 128 # Crenellated Burdock
    T5_TEASEL = 129 # Dragon Teasel
    T6_FOXGLOVE = 130 # Elusive Foxglove
    T7_MULLEIN = 131 # Firetouched Mullein
    T5_EGG = 135 # Goose Eggs
    T8_YARROW = 132 # Ghoul Yarrow
    T4_MILK = 134 # Goat's Milk
    T4_BUTTER = 899 # Goat's Butter
    T3_EGG = 133 # Hen Eggs
    T6_POTATO = 123 # Potatoes
    T8_PUMPKIN = 125 # Pumpkin
    T6_MILK = 136 # Sheep's Milk
    T6_BUTTER = 900 # Sheep's Butter

    T3_ALCHEMY_RARE_EAGLE = 1868 # Rugged Dawnfeather
    T5_ALCHEMY_RARE_EAGLE = 1869 # Fine Dawnfeather
    T7_ALCHEMY_RARE_EAGLE = 1870 # Excellent Dawnfeather
    T3_ALCHEMY_RARE_IMP = 1862 # Rugged Imp's Horn
    T5_ALCHEMY_RARE_IMP = 1863 # Fine Imp's Horn
    T7_ALCHEMY_RARE_IMP = 1864 # Excellent Imp's Horn
    T3_ALCHEMY_RARE_ELEMENTAL = 1865 # Rugged Runestone Tooth
    T5_ALCHEMY_RARE_ELEMENTAL = 1866 # Fine Runestone Tooth
    T7_ALCHEMY_RARE_ELEMENTAL = 1867 # Excellent Runestone Tooth
    T3_ALCHEMY_RARE_PANTHER = 1850 # Rugged Shadow Claws
    T5_ALCHEMY_RARE_PANTHER = 1851 # Fine Shadow Claws
    T7_ALCHEMY_RARE_PANTHER = 1852 # Excellent Shadow Claws
    T3_ALCHEMY_RARE_DIREBEAR = 1856 # Rugged Spirit Paws
    T5_ALCHEMY_RARE_DIREBEAR = 1857 # Fine Spirit Paws
    T7_ALCHEMY_RARE_DIREBEAR = 1858 # Excellent Spirit Paws
    T3_ALCHEMY_RARE_ENT = 1853 # Rugged Sylvian Root
    T5_ALCHEMY_RARE_ENT = 1854 # Fine Sylvian Root
    T7_ALCHEMY_RARE_ENT = 1855 # Excellent Sylvian Root
    T3_ALCHEMY_RARE_WEREWOLF = 1859 # Rugged Werewolf Fangs
    T5_ALCHEMY_RARE_WEREWOLF = 1860 # Fine Werewolf Fangs
    T7_ALCHEMY_RARE_WEREWOLF = 1861 # Excellent Werewolf Fangs

class Basic_Ingredients(Enum):
    T2_AGARIC = 126  # Arcane Agaric
    T3_COMFREY = 127 # Brightleaf Comfrey
    T8_BUTTER = 901 # Cow's Butter
    T8_MILK = 137 # Cow's Milk
    T7_CORN = 124 # Bundle of Corn
    T4_BURDOCK = 128 # Crenellated Burdock
    T5_TEASEL = 129 # Dragon Teasel
    T6_FOXGLOVE = 130 # Elusive Foxglove
    T7_MULLEIN = 131 # Firetouched Mullein
    T5_EGG = 135 # Goose Eggs
    T8_YARROW = 132 # Ghoul Yarrow
    T4_MILK = 134 # Goat's Milk
    T4_BUTTER = 899 # Goat's Butter
    T3_EGG = 133 # Hen Eggs
    T6_POTATO = 123 # Potatoes
    T8_PUMPKIN = 125 # Pumpkin
    T6_MILK = 136 # Sheep's Milk
    T6_BUTTER = 900 # Sheep's Butter

ingr_dict = {
    "T2_AGARIC": "Arcane Agaric",
    "T3_COMFREY": "Brightleaf Comfrey",
    "T8_BUTTER": "Cow's Butter",
    "T8_MILK": "Cow's Milk",
    "T7_CORN": "Bundle of Corn",
    "T4_BURDOCK": "Crenellated Burdock",
    "T5_TEASEL": "Dragon Teasel",
    "T6_FOXGLOVE": "Elusive Foxglove",
    "T7_MULLEIN": "Firetouched Mullein",
    "T5_EGG": "Goose Eggs",
    "T8_YARROW": "Ghoul Yarrow",
    "T4_MILK": "Goat's Milk",
    "T4_BUTTER": "Goat's Butter",
    "T3_EGG": "Hen Eggs",
    "T6_POTATO": "Potatoes",
    "T8_PUMPKIN": "Pumpkin",
    "T6_MILK": "Sheep's Milk",
    "T6_BUTTER": "Sheep's Butter",
    "T3_ALCHEMY_RARE_EAGLE": "Rugged Dawnfeather",
    "T5_ALCHEMY_RARE_EAGLE": "Fine Dawnfeather",
    "T7_ALCHEMY_RARE_EAGLE": "Excellent Dawnfeather",
    "T3_ALCHEMY_RARE_IMP": "Rugged Imp's Horn",
    "T5_ALCHEMY_RARE_IMP": "Fine Imp's Horn",
    "T7_ALCHEMY_RARE_IMP": "Excellent Imp's Horn",
    "T3_ALCHEMY_RARE_ELEMENTAL": "Rugged Runestone Tooth",
    "T5_ALCHEMY_RARE_ELEMENTAL": "Fine Runestone Tooth",
    "T7_ALCHEMY_RARE_ELEMENTAL": "Excellent Runestone Tooth",
    "T3_ALCHEMY_RARE_PANTHER": "Rugged Shadow Claws",
    "T5_ALCHEMY_RARE_PANTHER": "Fine Shadow Claws",
    "T7_ALCHEMY_RARE_PANTHER": "Excellent Shadow Claws",
    "T3_ALCHEMY_RARE_DIREBEAR": "Rugged Spirit Paws",
    "T5_ALCHEMY_RARE_DIREBEAR": "Fine Spirit Paws",
    "T7_ALCHEMY_RARE_DIREBEAR": "Excellent Spirit Paws",
    "T3_ALCHEMY_RARE_ENT": "Rugged Sylvian Root",
    "T5_ALCHEMY_RARE_ENT": "Fine Sylvian Root",
    "T7_ALCHEMY_RARE_ENT": "Excellent Sylvian Root",
    "T3_ALCHEMY_RARE_WEREWOLF": "Rugged Werewolf Fangs",
    "T5_ALCHEMY_RARE_WEREWOLF": "Fine Werewolf Fangs",
    "T7_ALCHEMY_RARE_WEREWOLF": "Excellent Werewolf Fangs"
}

def get_ingr_name(ingr_constant):
    return ingr_dict.get(ingr_constant, INGR_NAME_NOT_FOUND_ERR)

def get_ingrs_string():
    return ','.join(ingr.name for ingr in Ingredients)

def get_ingrs_names_array():
    ingrs = []
    for i in Ingredients:
        ingrs.append(get_ingr_name(i.name))
    return ingrs

# =================================
# ===          CITIES           ===
# =================================

class Cities(Enum):
    LYMHURST = "Lymhurst" 
    BRIDGEWATCH = "Bridgewatch"
    CAERLEON = "Caerleon"
    FORT_STERLING = "Fort Sterling"
    MARTLOCK = "Martlock"
    THETFORD = "Thetford"
    BRECILIEN = "Brecilien"

def find_enum_key_by_value(enum_class, value):
    for key in enum_class:
        if key.value == value:
            return key.name
    return None

neighbor_cities_dict = {
    Cities.THETFORD : [Cities.FORT_STERLING, Cities.MARTLOCK],
    Cities.FORT_STERLING : [Cities.THETFORD, Cities.LYMHURST],
    Cities.LYMHURST : [Cities.FORT_STERLING, Cities.BRIDGEWATCH],
    Cities.BRIDGEWATCH : [Cities.LYMHURST, Cities.MARTLOCK],
    Cities.MARTLOCK : [Cities.BRIDGEWATCH, Cities.THETFORD],
    Cities.BRECILIEN : [], # Assume no neighbors, since 2sided transport between city isn't safe
    Cities.CAERLEON : [] # Assume no neighbors, since 2sided transport between city isn't safe
}

# =================================
# ===         RECIPES          ===
# =================================

recipe_book = {
    Potions.T2_POTION_ENERGY: [ (Ingredients.T2_AGARIC, 8)],
    Potions.T2_POTION_HEAL: [ (Ingredients.T2_AGARIC, 8)],
    Potions.T3_POTION_REVIVE: [ (Ingredients.T3_COMFREY, 8)],
    Potions.T3_POTION_STONESKIN: [ (Ingredients.T3_COMFREY, 8)],
    Potions.T3_POTION_ACID: [(Ingredients.T3_COMFREY, 16),
                             (Ingredients.T3_ALCHEMY_RARE_DIREBEAR, 1)],
    Potions.T3_POTION_MOB_RESET: [(Ingredients.T3_COMFREY, 16),
                             (Ingredients.T3_ALCHEMY_RARE_PANTHER, 1)],
    Potions.T3_POTION_CLEANSE2: [(Ingredients.T3_COMFREY, 16),
                             (Ingredients.T3_ALCHEMY_RARE_ENT, 1)],
    Potions.T3_POTION_SLOWFIELD: [(Ingredients.T3_COMFREY, 8)],
    Potions.T4_POTION_ENERGY: [(Ingredients.T4_BURDOCK, 24),
                               (Ingredients.T4_MILK, 6)],
    Potions.T4_POTION_HEAL: [(Ingredients.T4_BURDOCK, 24),
                               (Ingredients.T3_EGG, 6)],
    Potions.T4_POTION_COOLDOWN: [(Ingredients.T4_BURDOCK, 8),
                               (Ingredients.T3_COMFREY, 4)],
    Potions.T4_POTION_GATHER: [(Ingredients.T4_BUTTER, 16),
                               (Ingredients.T3_ALCHEMY_RARE_ELEMENTAL, 1)],
    Potions.T4_POTION_LAVA: [(Ingredients.T4_MILK, 16),
                               (Ingredients.T3_ALCHEMY_RARE_IMP, 1)],
    Potions.T4_POTION_BERSERK: [(Ingredients.T4_BURDOCK, 16),
                               (Ingredients.T3_ALCHEMY_RARE_WEREWOLF, 1)],
    Potions.T4_POTION_TORNADO: [(Ingredients.T4_BURDOCK, 16),
                               (Ingredients.T3_ALCHEMY_RARE_EAGLE, 1)],
    Potions.T4_POTION_HEAL: [(Ingredients.T4_BURDOCK, 24),
                               (Ingredients.T3_EGG, 6)],
    Potions.T5_POTION_REVIVE: [(Ingredients.T5_TEASEL, 24),
                               (Ingredients.T4_BURDOCK, 12),
                               (Ingredients.T5_EGG, 6)],
    Potions.T5_POTION_STONESKIN: [(Ingredients.T5_TEASEL, 24),
                               (Ingredients.T4_BURDOCK, 12),
                               (Ingredients.T4_MILK, 6)],
    Potions.T5_POTION_SLOWFIELD: [(Ingredients.T5_TEASEL, 24),
                               (Ingredients.T4_BURDOCK, 12),
                               (Ingredients.T5_EGG, 6)],
    Potions.T5_POTION_ACID: [(Ingredients.T5_TEASEL, 48),
                               (Ingredients.T4_BURDOCK, 24),
                               (Ingredients.T4_MILK, 12),
                               (Ingredients.T5_ALCHEMY_RARE_DIREBEAR, 1)],
    Potions.T5_POTION_MOB_RESET: [(Ingredients.T5_TEASEL, 48),
                               (Ingredients.T4_BURDOCK, 24),
                               (Ingredients.T2_AGARIC, 12),
                               (Ingredients.T5_ALCHEMY_RARE_PANTHER, 1)],
    Potions.T5_POTION_CLEANSE2: [(Ingredients.T5_TEASEL, 48),
                               (Ingredients.T3_COMFREY, 24),
                               (Ingredients.T4_BUTTER, 12),
                               (Ingredients.T5_ALCHEMY_RARE_ENT, 1)],
    Potions.T5_POTION_REVIVE: [(Ingredients.T5_TEASEL, 24),
                               (Ingredients.T4_BURDOCK, 12),
                               (Ingredients.T5_EGG, 6)],
    Potions.T5_POTION_STONESKIN: [(Ingredients.T5_TEASEL, 24),
                               (Ingredients.T4_BURDOCK, 12),
                               (Ingredients.T4_MILK, 6)],
    Potions.T6_POTION_BERSERK: [(Ingredients.T6_FOXGLOVE, 48),
                               (Ingredients.T2_AGARIC, 24),
                               (Ingredients.T6_POTATO, 12),
                               (Ingredients.T5_ALCHEMY_RARE_WEREWOLF, 1)],
    Potions.T6_POTION_ENERGY: [(Ingredients.T6_FOXGLOVE, 72),
                               (Ingredients.T6_MILK, 18),
                               (Ingredients.T6_POTATO, 18)],
    Potions.T6_POTION_HEAL: [(Ingredients.T6_FOXGLOVE, 72),
                               (Ingredients.T5_EGG, 18),
                               (Ingredients.T6_POTATO, 18)],
    Potions.T6_POTION_COOLDOWN: [(Ingredients.T6_FOXGLOVE, 24),
                               (Ingredients.T5_TEASEL, 12),
                               (Ingredients.T3_COMFREY, 12),
                               (Ingredients.T6_MILK, 6)],
    Potions.T6_POTION_GATHER: [(Ingredients.T6_BUTTER, 48),
                               (Ingredients.T6_FOXGLOVE, 24),
                               (Ingredients.T5_TEASEL, 12),
                               (Ingredients.T5_ALCHEMY_RARE_ELEMENTAL, 1)],
    Potions.T6_POTION_LAVA: [(Ingredients.T6_MILK, 48),
                               (Ingredients.T6_FOXGLOVE, 24),
                               (Ingredients.T3_EGG, 12),
                               (Ingredients.T5_ALCHEMY_RARE_IMP, 1)],
    Potions.T6_POTION_TORNADO: [(Ingredients.T6_FOXGLOVE, 48),
                               (Ingredients.T5_TEASEL, 24),
                               (Ingredients.T3_EGG, 12),
                               (Ingredients.T5_ALCHEMY_RARE_EAGLE, 1)],
    Potions.T6_POTION_ENERGY: [(Ingredients.T6_FOXGLOVE, 72),
                               (Ingredients.T6_MILK, 18),
                               (Ingredients.T6_POTATO, 18)],
    Potions.T6_POTION_HEAL: [(Ingredients.T6_FOXGLOVE, 72),
                               (Ingredients.T5_EGG, 18),
                               (Ingredients.T6_POTATO, 18)],
    Potions.T6_POTION_COOLDOWN: [(Ingredients.T6_FOXGLOVE, 24),
                               (Ingredients.T5_TEASEL, 12),
                               (Ingredients.T3_COMFREY, 12),
                               (Ingredients.T6_MILK, 6)],
    Potions.T7_POTION_REVIVE: [(Ingredients.T7_MULLEIN, 72),
                               (Ingredients.T6_FOXGLOVE, 36),
                               (Ingredients.T5_EGG, 18),
                               (Ingredients.T7_CORN, 18)],
    Potions.T7_POTION_STONESKIN: [(Ingredients.T7_MULLEIN, 72),
                               (Ingredients.T6_FOXGLOVE, 36),
                               (Ingredients.T4_BURDOCK, 36),
                               (Ingredients.T6_MILK, 18),
                               (Ingredients.T7_CORN, 18)],
    Potions.T7_POTION_SLOWFIELD: [(Ingredients.T7_MULLEIN, 72),
                               (Ingredients.T6_FOXGLOVE, 36),
                               (Ingredients.T4_BURDOCK, 36),
                               (Ingredients.T5_EGG, 18),
                               (Ingredients.T7_CORN, 18)],
    Potions.T7_POTION_ACID: [(Ingredients.T7_MULLEIN, 144),
                               (Ingredients.T6_FOXGLOVE, 72),
                               (Ingredients.T6_POTATO, 72),
                               (Ingredients.T6_MILK, 36),
                               (Ingredients.T7_CORN, 36),
                               (Ingredients.T7_ALCHEMY_RARE_DIREBEAR, 1)],
    Potions.T7_POTION_MOB_RESET: [(Ingredients.T7_MULLEIN, 144),
                               (Ingredients.T6_FOXGLOVE, 72),
                               (Ingredients.T3_COMFREY, 72),
                               (Ingredients.T2_AGARIC, 36),
                               (Ingredients.T7_CORN, 36),
                               (Ingredients.T7_ALCHEMY_RARE_PANTHER, 1)],
    Potions.T7_POTION_CLEANSE2: [(Ingredients.T7_MULLEIN, 144),
                               (Ingredients.T4_BURDOCK, 72),
                               (Ingredients.T3_COMFREY, 72),
                               (Ingredients.T6_BUTTER, 36),
                               (Ingredients.T7_CORN, 36),
                               (Ingredients.T7_ALCHEMY_RARE_ENT, 1)],
    Potions.T7_POTION_REVIVE: [(Ingredients.T7_MULLEIN, 72),
                               (Ingredients.T6_FOXGLOVE, 36),
                               (Ingredients.T5_EGG, 18),
                               (Ingredients.T7_CORN, 18)],
    Potions.T7_POTION_STONESKIN: [(Ingredients.T7_MULLEIN, 72),
                               (Ingredients.T6_FOXGLOVE, 36),
                               (Ingredients.T4_BURDOCK, 36),
                               (Ingredients.T6_MILK, 18),
                               (Ingredients.T7_CORN, 18)],
    Potions.T7_POTION_SLOWFIELD: [(Ingredients.T7_MULLEIN, 72),
                               (Ingredients.T6_FOXGLOVE, 36),
                               (Ingredients.T4_BURDOCK, 36),
                               (Ingredients.T5_EGG, 18),
                               (Ingredients.T7_CORN, 18)],
    Potions.T8_POTION_BERSERK: [(Ingredients.T8_YARROW, 144),
                               (Ingredients.T3_COMFREY, 72),
                               (Ingredients.T6_POTATO, 72),
                               (Ingredients.T7_CORN, 36),
                               (Ingredients.T8_PUMPKIN, 36),
                               (Ingredients.T7_ALCHEMY_RARE_WEREWOLF, 1)],
    Potions.T8_POTION_CLEANSE: [(Ingredients.T8_YARROW, 72),
                               (Ingredients.T7_MULLEIN, 36),
                               (Ingredients.T5_TEASEL, 36),
                               (Ingredients.T8_MILK, 18),
                               (Ingredients.T8_PUMPKIN, 18)],
    Potions.T8_POTION_COOLDOWN: [(Ingredients.T8_YARROW, 72),
                               (Ingredients.T7_MULLEIN, 36),
                               (Ingredients.T5_TEASEL, 36),
                               (Ingredients.T8_MILK, 18),
                               (Ingredients.T8_PUMPKIN, 18)],
    Potions.T8_POTION_GATHER: [(Ingredients.T8_BUTTER, 144),
                               (Ingredients.T8_YARROW, 72),
                               (Ingredients.T7_MULLEIN, 72),
                               (Ingredients.T6_FOXGLOVE, 36),
                               (Ingredients.T8_PUMPKIN, 36),
                               (Ingredients.T7_ALCHEMY_RARE_ELEMENTAL, 1)],
    Potions.T8_POTION_LAVA: [(Ingredients.T8_MILK, 144),
                               (Ingredients.T8_YARROW, 72),
                               (Ingredients.T7_MULLEIN, 72),
                               (Ingredients.T5_EGG, 36),
                               (Ingredients.T8_PUMPKIN, 36),
                               (Ingredients.T7_ALCHEMY_RARE_IMP, 1)],
    Potions.T8_POTION_TORNADO: [(Ingredients.T8_YARROW, 144),
                               (Ingredients.T7_MULLEIN, 72),
                               (Ingredients.T7_CORN, 72),
                               (Ingredients.T5_EGG, 36),
                               (Ingredients.T8_PUMPKIN, 36),
                               (Ingredients.T7_ALCHEMY_RARE_EAGLE, 1)],
}

def get_recipe(potion):
    return recipe_book.get(potion, [])

def print_recipe(potion):
    recipe = get_recipe(potion)
    print(f"\nRecept pro {get_potion_name(potion.name)}:")
    for ingredient, amount in recipe:
        print(f"{get_ingr_name(ingredient.name)} - {amount}")

def get_crafted_amount(potion_enum):
    recipe = recipe_book.get(potion_enum, [])
    for ingredient, amount in recipe:
        if amount==1: return 10
    else: return 5

# =================================
# ===        NUTRIENTS          ===
# =================================

craft_costs = {
    Cities.BRECILIEN: 450, # 30.8.2024
    Cities.BRIDGEWATCH: 810,
    Cities.CAERLEON: 298, # 30.8.2024
    Cities.FORT_STERLING: 950, # 30.8.2024
    Cities.LYMHURST: 705,
    Cities.MARTLOCK: 950,
    Cities.THETFORD: 780 # 30.8.2024
}

def get_nutrients(potion_enum):
    recipe = get_recipe(potion_enum)
    nutrients = 0
    for ingredient, amount in recipe:
        if amount>1:
            nutrients += amount*45/1000
    return nutrients

def get_craft_cost(potion_name, city):
    potion_enum = Potions[potion_name] # získá enum podle Stringu
    if get_tier_from_potid(potion_enum.name) == '2': # Tier 2 potions get crafted for free
        return 0
    nutrients = get_nutrients(potion_enum)
    cost = craft_costs.get(city)
    total_cost = round(cost * nutrients,0)
    return (total_cost/get_crafted_amount(potion_enum))