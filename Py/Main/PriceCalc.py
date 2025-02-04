from datetime import *
from Enums import *
from Helper import *

# =================================
# =====      CONSTANTS        =====
# =================================

def get_sell_tax():
    if PREMIUM: return 0.04 # 4%
    else: return 0.08 # 8%

SETUP_FEE = 0.025 # 2,5%

def get_return_rate(city):
    if city == Cities.BRECILIEN: return 0.248 # 24,8%
    elif city in Cities.__members__: return 0.152 # 15,2%
    else: return 0 # 0%

# =================================
# =====      TIMESTAMP        =====
# =================================

# Tell me how many hours ago has the timestamp been printed
def timestamp_ago(timestamp_str):
    timestamp_dt = datetime.fromisoformat(timestamp_str)
    now = datetime.now()
    time_diff = now - timestamp_dt # [s]
    time_diff = time_diff.total_seconds() / 3600 # [h]
    time_diff = round(time_diff, 2)
    return time_diff

# Adds hours to a timestamp
def timestamp_add_hours(timestamp_str, h):
    timestamp_dt = datetime.fromisoformat(timestamp_str)
    new_timestamp_dt = timestamp_dt + timedelta(hours=h) # Přidání 2 hodin pomocí objektu timedelta
    new_timestamp_str = new_timestamp_dt.isoformat() # Převedení zpět na formát ISO 8601
    return new_timestamp_str

# =================================
# =====      CASH FLOW       =====
# =================================

def calculate_cashflow(history_df):
    df = history_df
    df["Cashflow"] = df["Avg_Price"]*df["Count"]
    df["Cashflow_Display"] = df["Cashflow"].apply(format_cashflow)
    df = df.sort_values(by="Cashflow", ascending=False)
    #df = df.sort_values(by="Cashflow", ascending=False)
    return df

# Funkce pro formátování
def format_cashflow(value):
    if value >= 1_000_000 or value <= -1_000_000:
        return f"{value/1_000_000:.1f}M"
    elif value >= 1_000 or value <= -1_000:
        return f"{value/1_000:.1f}k"
    else:
        return str(f"{value:.1f}")


# =================================
# =====    MATERIAL COST      =====
# =================================

# Přidání sloupce Ingr_cost
def get_ingr_cost(pot_prices_df, ingr_prices_df, city):
    df = pot_prices_df
    df['Ingr_cost'] = df['Item_id'].apply(calculate_ingr_cost, df_ingr=ingr_prices_df, city=city)
    return df

def calculate_ingr_cost(potion_name, df_ingr, city):
    potion_enum = Potions[potion_name]  # Získání odpovídajícího enumu
    recipe = recipe_book.get(potion_enum, [])
    total_cost = 0
    for ingredient, amount in recipe:
        rrr = 0
        if amount > 1:
            rrr = get_return_rate(city)
        ingredient_name = ingredient.name  # Převod enumu na název (řetězec)
        ingredient_cost = df_ingr.loc[df_ingr['Item_id'] == ingredient_name, 'Price'].values[0]
        total_cost += ingredient_cost * amount/ (1+rrr)
    return (total_cost/get_crafted_amount(potion_enum))

# =================================
# ===    PROFIT CALCULATION     ===
# =================================

def calc_earned(pot_prices_df):
    df = pot_prices_df
    df['Earned'] = df['Price']*(1-SETUP_FEE)*(1-get_sell_tax()) # Return rate is now considered in Material Cost
    return df

def calc_profit(pot_prices_df, location):
    df = calc_earned(pot_prices_df)
    df["Craft_cost"] = df["Item_id"].apply(get_craft_cost, city=location)
    df["Create_cost"] = df['Ingr_cost'] + df["Craft_cost"]
    df['Profit'] = df['Earned'] - df["Create_cost"]
    df['Profit_perc'] = df['Profit']/(df['Create_cost'])*100
    return df

def calc_potential(pot_prices_df):
    df = pot_prices_df
    df["Potential"] = (df['Count'] * df['Profit']) / (CASHFLOW_INTERVAL-1)
    df["Potential_h"] = df["Potential"].apply(format_cashflow)
    return df