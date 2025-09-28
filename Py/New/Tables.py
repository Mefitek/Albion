import pandas as pd
from pathlib import Path # reading from csv
import csv # reading from csv
import ast

# =========================================================
# ===========       Items Dictionary          ===========
# =========================================================
"""
df_pots_dic
| Name : Str | Constant : Str | ID : int | tier : int | weight : float |
"""
def init_pots_dict():
    # define dataframe
    df =  pd.DataFrame ({"Name": pd.Series(dtype="string"),
                        "Constant": pd.Series(dtype="float64"),
                        "ID": pd.Series(dtype="int64"),
                        "tier": pd.Series(dtype="int64"),
                        "weight": pd.Series(dtype="float64")})
    # Get potions data
    file_name = 'potions.csv'
    csv_file_path = Path(__file__).parent / 'data' / file_name
    with open(csv_file_path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            df = df._append({"Name": row['Name'],
                            "Constant": row['Constant'],
                            "ID": int(row['ID']),
                            "tier": int(row['tier']),
                            "weight": float(row['weight'])
                            }, ignore_index=True)
    return df

def init_ingr_dict():
    # define dataframe
    df =  pd.DataFrame ({"Name": pd.Series(dtype="string"),
                        "Constant": pd.Series(dtype="float64"),
                        "ID": pd.Series(dtype="int64"),
                        "tier": pd.Series(dtype="int64"),
                        "weight": pd.Series(dtype="float64")})
    # Get ingredients data
    file_name = 'potions.csv'
    csv_file_path = Path(__file__).parent / 'data' / file_name
    with open(csv_file_path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            df = df._append({"Name": row['Name'],
                            "Constant": row['Constant'],
                            "ID": int(row['ID']),
                            "tier": 0,
                            "weight": 0.0
                            }, ignore_index=True)
    return df

def get_recipe_book():
    # define dataframe
    df =  pd.DataFrame ({"Constant": pd.Series(dtype="str"),
                        "Recipe": pd.Series(dtype="str")})
    # Get recipes data
    file_name = 'recipes.csv'
    csv_file_path = Path(__file__).parent / 'data' / file_name
    with open(csv_file_path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            #recipe = ast.literal_eval(row['Recipe'])
            recipe = row['Recipe']
            df = df._append({
                "Constant": row['Constant'],
                "Recipe": recipe
            }, ignore_index=True)
    return df

# =========================================================

