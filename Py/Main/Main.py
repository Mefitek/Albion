from API1 import *
from Enums import *
import PriceScan
import PriceCalc
import pandas
import time

city = Cities.CAERLEON


def get_history_df(city):
    df_history = get_prices_history(city.value, POTIONS)
    df_history = PriceCalc.calculate_cashflow(df_history)
    return df_history

def get_pot_prices(city):
    pot_df = get_prices_current(city, POTIONS)
    ingr_df = get_prices_current(city, INGREDIENTS)
    df = PriceCalc.get_ingr_cost(pot_df, ingr_df, city) # calculate ingredient costs
    df = PriceCalc.calc_profit(df, city) # calculate profits
    return df

def get_full_df(city):
    df_history = get_history_df(city)
    df = get_pot_prices(city)
    df_merged = pandas.merge(df, df_history[['Item_name', 'Count', 'Cashflow', 'Cashflow_Display']], on='Item_name', how='left')
    df_merged = PriceCalc.calc_potential(df_merged)
    df_merged = df_merged.sort_values(by="Profit_perc", ascending=False)
    #df_merged = df_merged.sort_values(by="Potential", ascending=False)
    return df_merged

def scan():
    time.sleep(7)
    PriceScan.scan_prices_potions()
    PriceScan.scan_prices_ingredients()

def shortscan():
    time.sleep(3)
    PriceScan.scan_prices_potions_special()

def show_history():
    df_history = get_history_df(city)
    print(df_history)

def show(picked_city):
    df = get_full_df(picked_city)
    df = df[['Location','Item_name','Create_cost','Price', 'Earned','Profit','Cashflow_Display', 'Profit_perc','Ago', 'Potential_h']]
    print(df)

#scan()
#shortscan()
show(Cities.BRECILIEN)
#show_history()
