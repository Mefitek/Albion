from enum import *

# =================================
# ===         POTIONS           ===
# =================================

class Potions(Enum):
    T2_POTION_HEAL = 469  # Minor Healing Potion
    T2_POTION_ENERGY = 474  # Minor Energy Potion
    T3_POTION_ACID = 623 # Minor Acid Potion
    T3_POTION_REVIVE = 479  # Minor Gigantify Potion
    T3_POTION_STONESKIN = 484  # Minor Resistance Potion
    T3_POTION_SLOWFIELD = 489  # Minor Sticky Potion
    T3_POTION_MOB_RESET = 599 # Minor Calming Potion
    T3_POTION_CLEANSE2 = 611 # Minor Cleansing Potion
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

# Function to get potion name from potion constant
def get_potion_name(potion_constant):
    return potion_dict.get(potion_constant, "Potion not found")

def get_potions_array():
    POTS = []
    for p in Potions:
        POTS.append(p.name)
    return POTS

def get_potions_string():
    return ','.join(potion.name for potion in Potions)

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
