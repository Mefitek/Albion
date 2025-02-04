from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Vytvoření SparkSession
spark = SparkSession.builder \
    .appName("Elixirs DataFrame") \
    .getOrCreate()

# Data
data = [
    (482, 2, "T2_POTION_HEAL", "Minor Healing Potion"),
    (486, 4, "T4_POTION_HEAL", "Healing Potion"),
    (490, 6, "T6_POTION_HEAL", "Major Healing Potion"),
    (494, 2, "T2_POTION_ENERGY", "Minor Energy Potion"),
    (498, 4, "T4_POTION_ENERGY", "Energy Potion"),
    (502, 6, "T6_POTION_ENERGY", "Major Energy Potion"),
    (506, 3, "T3_POTION_REVIVE", "Minor Gigantify Potion"),
    (510, 5, "T5_POTION_REVIVE", "Gigantify Potion"),
    (514, 7, "T7_POTION_REVIVE", "Major Gigantify Potion"),
    (518, 3, "T3_POTION_STONESKIN", "Minor Resistance Potion"),
    (522, 5, "T5_POTION_STONESKIN", "Resistance Potion"),
    (526, 7, "T7_POTION_STONESKIN", "Major Resistance Potion"),
    (530, 3, "T3_POTION_SLOWFIELD", "Minor Sticky Potion"),
    (534, 5, "T5_POTION_SLOWFIELD", "Sticky Potion"),
    (538, 7, "T7_POTION_SLOWFIELD", "Major Sticky Potion"),
    (542, 4, "T4_POTION_COOLDOWN", "Minor Poison Potion"),
    (546, 6, "T6_POTION_COOLDOWN", "Poison Potion"),
    (550, 8, "T8_POTION_COOLDOWN", "Major Poison Potion"),
    (554, 8, "T8_POTION_CLEANSE", "Invisibility Potion"),
    (558, 3, "T3_POTION_MOB_RESET", "Minor Calming Potion"),
    (562, 5, "T5_POTION_MOB_RESET", "Calming Potion"),
    (566, 7, "T7_POTION_MOB_RESET", "Major Calming Potion"),
    (570, 3, "T3_POTION_CLEANSE2", "Minor Cleansing Potion"),
    (574, 5, "T5_POTION_CLEANSE2", "Cleansing Potion"),
    (578, 7, "T7_POTION_CLEANSE2", "Major Cleansing Potion"),
    (582, 3, "T3_POTION_ACID", "Minor Acid Potion"),
    (586, 5, "T5_POTION_ACID", "Acid Potion"),
    (590, 7, "T7_POTION_ACID", "Major Acid Potion"),
    (594, 4, "T4_POTION_BERSERK", "Minor Berserk Potion"),
    (598, 6, "T6_POTION_BERSERK", "Berserk Potion"),
    (602, 8, "T8_POTION_BERSERK", "Major Berserk Potion"),
    (606, 4, "T4_POTION_LAVA", "Minor Hellfire Potion"),
    (610, 6, "T6_POTION_LAVA", "Hellfire Potion"),
    (614, 8, "T8_POTION_LAVA", "Major Hellfire Potion"),
    (618, 4, "T4_POTION_GATHER", "Minor Gathering Potion"),
    (622, 6, "T6_POTION_GATHER", "Gathering Potion"),
    (626, 8, "T8_POTION_GATHER", "Major Gathering Potion")
]

# Vytvoření DataFrame
columns = ["id", "tier", "id_name", "name"]
elixirs_df = spark.createDataFrame(data, columns)

# Funkce pro výpis obsahu DataFrame
def print_elixirs_df(df):
    df.select("id", "tier", "id_name", "name").show(truncate=False)

# Výpis obsahu DataFrame
print_elixirs_df(elixirs_df)

# Ukončení SparkSession
spark.stop()

'''
# Python list obsahující elixíry
# funguje - zkusím ještě jako python data frame?
elixirs = [
    {"id": 482, "tier": 2, "id_name": "T2_POTION_HEAL", "name": "Minor Healing Potion"},
    {"id": 486, "tier": 4, "id_name": "T4_POTION_HEAL", "name": "Healing Potion"},
    {"id": 490, "tier": 6, "id_name": "T6_POTION_HEAL", "name": "Major Healing Potion"},
    {"id": 494, "tier": 2, "id_name": "T2_POTION_ENERGY", "name": "Minor Energy Potion"},
    {"id": 498, "tier": 4, "id_name": "T4_POTION_ENERGY", "name": "Energy Potion"},
    {"id": 502, "tier": 6, "id_name": "T6_POTION_ENERGY", "name": "Major Energy Potion"},
    {"id": 506, "tier": 3, "id_name": "T3_POTION_REVIVE", "name": "Minor Gigantify Potion"},
    {"id": 510, "tier": 5, "id_name": "T5_POTION_REVIVE", "name": "Gigantify Potion"},
    {"id": 514, "tier": 7, "id_name": "T7_POTION_REVIVE", "name": "Major Gigantify Potion"},
    {"id": 518, "tier": 3, "id_name": "T3_POTION_STONESKIN", "name": "Minor Resistance Potion"},
    {"id": 522, "tier": 5, "id_name": "T5_POTION_STONESKIN", "name": "Resistance Potion"},
    {"id": 526, "tier": 7, "id_name": "T7_POTION_STONESKIN", "name": "Major Resistance Potion"},
    {"id": 530, "tier": 3, "id_name": "T3_POTION_SLOWFIELD", "name": "Minor Sticky Potion"},
    {"id": 534, "tier": 5, "id_name": "T5_POTION_SLOWFIELD", "name": "Sticky Potion"},
    {"id": 538, "tier": 7, "id_name": "T7_POTION_SLOWFIELD", "name": "Major Sticky Potion"},
    {"id": 542, "tier": 4, "id_name": "T4_POTION_COOLDOWN", "name": "Minor Poison Potion"},
    {"id": 546, "tier": 6, "id_name": "T6_POTION_COOLDOWN", "name": "Poison Potion"},
    {"id": 550, "tier": 8, "id_name": "T8_POTION_COOLDOWN", "name": "Major Poison Potion"},
    {"id": 554, "tier": 8, "id_name": "T8_POTION_CLEANSE", "name": "Invisibility Potion"},
    {"id": 558, "tier": 3, "id_name": "T3_POTION_MOB_RESET", "name": "Minor Calming Potion"},
    {"id": 562, "tier": 5, "id_name": "T5_POTION_MOB_RESET", "name": "Calming Potion"},
    {"id": 566, "tier": 7, "id_name": "T7_POTION_MOB_RESET", "name": "Major Calming Potion"},
    {"id": 570, "tier": 3, "id_name": "T3_POTION_CLEANSE2", "name": "Minor Cleansing Potion"},
    {"id": 574, "tier": 5, "id_name": "T5_POTION_CLEANSE2", "name": "Cleansing Potion"},
    {"id": 578, "tier": 7, "id_name": "T7_POTION_CLEANSE2", "name": "Major Cleansing Potion"},
    {"id": 582, "tier": 3, "id_name": "T3_POTION_ACID", "name": "Minor Acid Potion"},
    {"id": 586, "tier": 5, "id_name": "T5_POTION_ACID", "name": "Acid Potion"},
    {"id": 590, "tier": 7, "id_name": "T7_POTION_ACID", "name": "Major Acid Potion"},
    {"id": 594, "tier": 4, "id_name": "T4_POTION_BERSERK", "name": "Minor Berserk Potion"},
    {"id": 598, "tier": 6, "id_name": "T6_POTION_BERSERK", "name": "Berserk Potion"},
    {"id": 602, "tier": 8, "id_name": "T8_POTION_BERSERK", "name": "Major Berserk Potion"},
    {"id": 606, "tier": 4, "id_name": "T4_POTION_LAVA", "name": "Minor Hellfire Potion"},
    {"id": 610, "tier": 6, "id_name": "T6_POTION_LAVA", "name": "Hellfire Potion"},
    {"id": 614, "tier": 8, "id_name": "T8_POTION_LAVA", "name": "Major Hellfire Potion"},
    {"id": 618, "tier": 4, "id_name": "T4_POTION_GATHER", "name": "Minor Gathering Potion"},
    {"id": 622, "tier": 6, "id_name": "T6_POTION_GATHER", "name": "Gathering Potion"},
    {"id": 626, "tier": 8, "id_name": "T8_POTION_GATHER", "name": "Major Gathering Potion"}
]

# Funkce pro výpis obsahu listu elixírů
def print_elixirs(elixirs):
    for elixir in elixirs:
        print(f"ID: {elixir['id']}, Tier: {elixir['tier']}, ID Name: {elixir['id_name']}, Name: {elixir['name']}")

# Výpis obsahu listu elixírů
print_elixirs(elixirs)
'''