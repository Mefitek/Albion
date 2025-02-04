import requests
import datetime
from datetime import datetime, timedelta
from Enums import *
import pandas
import PriceCalc
from Helper import *

POTIONS = get_potions_string()
INGREDIENTS = get_ingrs_string()

def get_last24h_data(data, hours):
    avg_price = 0
    item_count = 0
    valid_hours = min(hours, len(data)) # Zajistěte, že nebudete sáhat mimo rozsah
    for i in range(-valid_hours, 0):  # Iterace od -valid_hours do -1
        count = data[i]["item_count"]
        avg_price += (data[i]["avg_price"]) * count
        item_count += count
    if item_count == 0: # Ochrana před dělením nulou
        return 0, 0
    avg_price = avg_price / item_count
    return avg_price, item_count

# This function gets the last hour's average price of all potions in a given city
# return a pandas dataframe
def get_prices_history(city, items_of_interest):

    df = pandas.DataFrame(columns=["Location", "Item_name", "Item_id", "Avg_Price", "Count", "Timestamp", "Ago"])

    print("\n\nSENDING API REQUEST\n\n")
    # Request data from the Albion Online API
    req_url = HISTORY_URL + items_of_interest + '.json?&locations=' + city + '&qualities=' + QUALITY + '&time-scale=' + TIME_SCALE
    current_history_response = requests.get(req_url)

    # Check if the request was successful
    if current_history_response.status_code == 200:
        # Extract the market prices from the response data
        for element in current_history_response.json():
            location = element["location"]
            item_id = element["item_id"]
            item_name = get_item_name(item_id)
            data = element["data"]
            # -1 = last record (last hour)

            #avg_price = data[-1]["avg_price"]
            #item_count = data[-1]["item_count"]
            avg_price, item_count = get_last24h_data(data, CASHFLOW_INTERVAL)

            timestamp = PriceCalc.timestamp_add_hours(data[-1]["timestamp"],2)
            df = df._append({"Location": location,
                            "Item_name": item_name,
                            "Item_id": item_id,
                            "Avg_Price": avg_price,
                            "Count": item_count,
                            "Timestamp": timestamp,
                            "Ago": PriceCalc.timestamp_ago(timestamp)
                            }, ignore_index=True)
        
    else:
        print("Failed to retrieve market data from Albion Online API")
    
    return(df)

def get_prices_history_old(city, items_of_interest):

    df = pandas.DataFrame(columns=["Location", "Item_name", "Item_id", "Avg_Price", "Count", "Timestamp", "Ago"])

    print("\n\nSENDING API REQUEST\n\n")
    # Request data from the Albion Online API
    req_url = HISTORY_URL + items_of_interest + '.json?&locations=' + city + '&qualities=' + QUALITY + '&time-scale=' + TIME_SCALE
    current_history_response = requests.get(req_url)

    # Check if the request was successful
    if current_history_response.status_code == 200:
        # Extract the market prices from the response data
        for element in current_history_response.json():
            location = element["location"]
            item_id = element["item_id"]
            item_name = get_item_name(item_id)
            data = element["data"]
            # -1 = last record (last hour)
            avg_price = data[-1]["avg_price"]
            item_count = data[-1]["item_count"]
            timestamp = PriceCalc.timestamp_add_hours(data[-1]["timestamp"],2)
            df = df._append({"Location": location,
                            "Item_name": item_name,
                            "Item_id": item_id,
                            "Avg_Price": avg_price,
                            "Count": item_count,
                            "Timestamp": timestamp,
                            "Ago": PriceCalc.timestamp_ago(timestamp)
                            }, ignore_index=True)
        
    else:
        print("Failed to retrieve market data from Albion Online API")
    
    return(df)

# Gets the current price of all potions in given city
# return Pandas dataframe
def get_prices_current(city, items_of_interest):
    df = pandas.DataFrame(columns=["Location", "Item_name","Item_id", "Price", "Timestamp", "Ago"])
    req_url = PRICE_URL + items_of_interest + '.json?&locations=' + city.value + '&qualities=' + QUALITY
    current_price_response = requests.get(req_url)

    if current_price_response.status_code == 200: # If the request was successful

        for element in current_price_response.json():
            location = element["city"]
            item_id = element["item_id"]
            item_name = get_item_name(item_id)
            price = element["sell_price_min"]
            timestamp = PriceCalc.timestamp_add_hours(element["sell_price_min_date"],2)

            df = df._append({"Location": location,
                            "Item_name": item_name,
                            "Item_id": item_id,
                            "Price": price,
                            "Timestamp": timestamp,
                            "Ago": PriceCalc.timestamp_ago(timestamp)
                            }, ignore_index=True)
    else:
        print("Failed to retrieve market data from Albion Online API")
    
    return(df)

def get_item_name(item_id):
    name = get_potion_name(item_id)
    if name == POT_NAME_NOT_FOUND_ERR:
        name = get_ingr_name(item_id)
        if name == INGR_NAME_NOT_FOUND_ERR:
            name = "UKNOWN ITEM"
    return name
