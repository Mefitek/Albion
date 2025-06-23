'''
WORK IN PROGRESS
Chtěl bych nahradit napevno psané dictionaries v Enums.py tak
aby se data vyčítala z csv souborů

'''

from dataclasses import dataclass

from pathlib import Path # reading from csv
import csv # reading from csv

import numpy as np


@dataclass
class Item:
    """ Class that holds data about Albion items """
    name : str      # Minor Energy Potion
    const : str     # T2_POTION_ENERGY
    ID : int        # 474
    weight : float

@dataclass
class Potion(Item):
    """ Items as individual potions """
    weight : float


def init_potions(file_name = 'potions.csv'):
    csv_file_path = Path(__file__).parent / 'data' / file_name
    pots = []
    with open(csv_file_path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            pot = Potion(name = row['Name'],
                         const = row['Constant'],
                         ID = row['ID'],
                         weight = 0.0) # TODO: Weight
            pots.append(pot)
    return pots

