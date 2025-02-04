import requests
import datetime
from datetime import datetime, timedelta
from API.Main.Help import *

# /api/v2/stats/history/T4_BAG,T5_BAG.json?date=2-5-2020&end_date=2-12-2020&locations=Caerleon&qualities=2&time-scale=6

# API endpoint for the Albion Online data
BASE_URL = "http://europe.albion-online-data.com"
HISTORY_URL = BASE_URL + "/api/v2/stats/history/"
DATE_FROM = '3-6-2024'
DATE_TO = '10-6-2024'
DATES = '.json?date=' + DATE_FROM +'&end_date=' + DATE_TO
TIME_SCALE = str(6) # Hourly=1 , Daily = 24

# The item you want to the the market prices for
# https://github.com/ao-data/ao-bin-dumps/tree/master/formatted
#ITEMS_OF_INTEREST = get_potions()
ITEMS_OF_INTEREST = ['T8_POTION_CLEANSE']

# The location you want to look for
LOCATION = 'Caerleon'

# Use quality 0 or 2 for non-equipment items
QUALITY = '0'


curr_prices = {}
result = []

for item in ITEMS_OF_INTEREST:
    item_name = item

    # Request data from the Albion Online API
    req_url = HISTORY_URL + item_name + DATES + '&locations=' + LOCATION + '&qualities=' + QUALITY + '&time-scale=' + TIME_SCALE
    #req_url = req_url + '&time-scale=24'
    current_price_response = requests.get(req_url)


    # Check if the request was successful
    if current_price_response.status_code == 200:
        # Extract the market prices from the response data
        print(current_price_response.json())
        market_prices = current_price_response.json()[0]["sell_price_min"]
        prices_date = current_price_response.json()[0]["sell_price_min_date"]
        city = current_price_response.json()[0]["city"]
        print(f"\n{item_name} ({city}) : {market_prices} - {prices_date}\n")
        curr_prices[item] = {
            'Item Name': item_name,
            'Current Price': market_prices
        }
    else:
        print("Failed to retrieve market data from Albion Online API")