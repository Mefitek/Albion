from Enums import *
from API1 import *
import pandas
from PriceCalc import *

# =================================
# =====      CONSTANTS        =====
# =================================

POTIONS = (','.join(potion.name for potion in BigFive))
INGRS = (','.join(ingr.name for ingr in Basic_Ingredients))
CITIES = [
    Cities.THETFORD,
    Cities.FORT_STERLING,
    Cities.LYMHURST,
    Cities.BRIDGEWATCH,
    Cities.MARTLOCK
]

# ========================================
# ===    2 BLUE NEIGHBORING CITIES     ===
# ========================================

# ["Location", "Item_name","Item_id", "Price", "Timestamp", "Ago"]
# "Craft String"

def get_all_prices(cities):
    df_pots = pandas.DataFrame(columns=["Location", "Item_name","Item_id", "Price", "Ago"])
    df_ingrs = pandas.DataFrame(columns=["Location", "Item_name","Item_id", "Price", "Ago"])
    for city in cities:
        df1 = get_prices_current(city, POTIONS)
        df2 = get_prices_current(city, INGRS)
        df_pots = pandas.concat([df_pots, df1], ignore_index=True)
        df_ingrs = pandas.concat([df_ingrs, df2], ignore_index=True)
    return df_pots, df_ingrs

def get_neigh_pairs(cities):
    pairs = []
    for city in cities:
        neighbors = neighbor_cities_dict.get(city, [])
        for neighbor in neighbors:
            c = city.value
            n = neighbor.value
            element1 = [c, n]
            element2 = [n, c]
            if not ((element1 in pairs) or (element2 in pairs)):
                pairs.append(element1)
    return pairs

def get_high_price(df_pots, pot, city_pair):
    city1 = city_pair[0]
    city2 = city_pair[1]
    df = df_pots[df_pots['Item_id'] == pot.name]
    df = df[(df['Location'] == city1) | (df['Location'] == city2)]
    max_price_row = df.loc[df['Price'].idxmax()]
    max_price_location = max_price_row['Location']
    max_price = max_price_row['Price']
    return max_price_location, max_price

def get_ingr_costs(potion_id, df_ingrs, city_pair):
    potion_enum = Potions[potion_id]
    recipe = recipe_book.get(potion_enum, [])
    total_ingr_cost = 0
    ingr_string = ""
    for ingredient, amount in recipe:
        rrr = 0 # Resource Return Rate
        city_id = find_enum_key_by_value(Cities, city_pair[0])
        if amount > 1:
            rrr = get_return_rate(city_id) # Rework if Brecilien is considered
        ingredient_id = ingredient.name  # Převod enumu na název (řetězec)
        city1 = city_pair[0]
        city2 = city_pair[1]
        df = df_ingrs[df_ingrs['Item_id'] == ingredient_id]
        df = df[(df['Location'] == city1) | (df['Location'] == city2)]
        min_price_row = df.loc[df['Price'].idxmax()]
        min_price_location = min_price_row['Location']
        min_price = min_price_row['Price']

        total_ingr_cost += min_price * amount / (1+rrr)
        #ingr_string += f"[{get_ingr_name(ingredient.name)}-{min_price_location}-{min_price}] " # is price needed here?
        ingr_string += f"[{min_price_location}] " # is price needed here?
    ingr_cost_one_pot = total_ingr_cost/get_crafted_amount(potion_enum)
    return (ingr_cost_one_pot, ingr_string)

def get_craft_costs(potion_id, city_pair):
    city1_id = Cities[find_enum_key_by_value(Cities, city_pair[0])]
    city2_id = Cities[find_enum_key_by_value(Cities, city_pair[1])]
    cost1 = get_craft_cost(potion_id, city1_id)
    cost2 = get_craft_cost(potion_id, city2_id)
    if cost1 < cost2:
        return (cost1, city1_id)
    return (cost2, city2_id)


def calc_neighbor():
    df_pots, df_ingrs = get_all_prices(CITIES)
    df = pandas.DataFrame(columns=["Location_1","Location_Sell", "Item_name","Item_id", "Price", "Earned", "Profit", "Ingr_Cost", "Craft_cost", "Ago", "Ingr_string", "Craft_string"])
    for pot in BigFive:
        pairs = get_neigh_pairs(CITIES)
        for pair in pairs:
            # higher Sell Price
            city_sell, max_price = get_high_price(df_pots, pot, pair)
            city1 = pair[1] if city_sell == pair[0] else pair[0]
            # lower Ingredients price
            ingr_cost_one_pot, ingr_string = get_ingr_costs(pot.name, df_ingrs, pair)
            craft_cost, craft_place = get_craft_costs(pot.name, pair)
            earned = (max_price)*(1-SETUP_FEE)*(1-get_sell_tax())
            profit = earned - craft_cost - ingr_cost_one_pot
            df = df._append({   "Location_1": city1,
                                "Location_Sell": city_sell,
                                "Item_name": get_potion_name(pot.name),
                                "Item_id": pot.name,
                                "Price": max_price,
                                "Earned": earned,
                                "Profit": profit,
                                "Ingr_Cost": ingr_cost_one_pot,
                                "Ingr_Cost": craft_cost,
                                "Timestamp": '0',
                                "Ago": '0',
                                "Ingr_string": ingr_string,
                                "Craft_string": craft_place
                                }, ignore_index=True)
    
    return df

df = calc_neighbor()
df = df[['Item_name','Price', 'Earned','Profit']]
print(df)

# ======================================
# =====    BRECILIEN TELEPORT      =====
# ======================================

BLUE_CITIES = [Cities.BRIDGEWATCH, Cities.FORT_STERLING, Cities.LYMHURST, Cities.MARTLOCK, Cities.THETFORD]
TELEPORT_CITIES = BLUE_CITIES + [Cities.BRECILIEN]
TELEPORT_TO_BRECI = False # If profits are big enough it might be worth it to teleport
POTS_OF_INTEREST = BigFive


# To brecilien you go on foot
def calc_breci_trans():
    df = pandas.DataFrame(columns=["Locations", "Item_name","Item_id", "Buy_cost", "Earned", "Profit", "Profit_perc"])
    df_pots, df_ingrs = get_all_prices(TELEPORT_CITIES)
    df_breci = df_pots[ df_pots["Location"] == Cities.BRECILIEN.value ]
    for city in BLUE_CITIES:
        df_blue = df_pots[ df_pots["Location"] == city.value ]
        for pot in POTS_OF_INTEREST:
            df_blue1 = df_blue[ df_blue["Item_id"] == pot.name ]
            df_breci1 = df_breci[ df_breci["Item_id"] == pot.name ]
            df = calc_breci_trans_prices(df_blue1, df_breci1, df)
    df = df.sort_values(by="Profit_perc", ascending=False)
    return df

def calc_breci_trans_prices(df_blue, df_breci, df):
    output_df = df
    buy_blue = df_blue['Price'].iloc[0]
    buy_breci = df_breci['Price'].iloc[0]
    blue_city_enum = Cities[find_enum_key_by_value(Cities, df_blue['Location'].iloc[0])]
    item_id = df_blue['Item_id'].iloc[0]
    item_name = df_blue['Item_name'].iloc[0]
    pot_weight = potion_weight_dict[BigFive[item_id]]

    # 1 - TO Brecilien
    loc = str(blue_city_enum.value) + " → " + str(Cities.BRECILIEN.value)
    buy_cost = buy_blue
    earned = buy_breci*(1-SETUP_FEE)*(1-get_sell_tax())
    if TELEPORT_TO_BRECI:
        transport_cost = pot_weight*300
    else:
        transport_cost = 0
    profit = earned - buy_cost - transport_cost
    profit_perc = round(profit/(buy_cost)*100,1)

    # 1 - Append
    output_df = output_df._append({ "Locations": loc,
                     "Item_name": item_name,
                     "Item_id": item_id,
                     "Buy_cost": buy_cost,
                     "Earned": earned,
                     "Profit": profit,
                     "Profit_perc": profit_perc
                    }, ignore_index=True)

    # 2 - FROM Brecilien
    loc = str(Cities.BRECILIEN.value) + " → " + str(blue_city_enum.value)
    buy_cost = buy_breci
    earned = buy_blue*(1-SETUP_FEE)*(1-get_sell_tax())
    transport_cost = pot_weight*300
    profit = earned - buy_cost - transport_cost
    profit_perc = round(profit/(buy_cost)*100,1)
    
    # 2 - Append
    output_df = output_df._append({ "Locations": loc,
                     "Item_name": item_name,
                     "Item_id": item_id,
                     "Buy_cost": buy_cost,
                     "Earned": earned,
                     "Profit": profit,
                     "Profit_perc": profit_perc
                    }, ignore_index=True)
    return output_df

# TODO: CALCULATE AGO
#df = calc_breci_trans()
#print(df)