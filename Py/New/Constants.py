PREMIUM = True

INGR_NAME_NOT_FOUND_ERR = "Ingredient not found"
POT_NAME_NOT_FOUND_ERR = "Potion not found"
CASHFLOW_INTERVAL = 4 # How many hours for cashflow consideration

# ==========   API CONSTANTS   =============
HISTORY_URL = "http://europe.albion-online-data.com/api/v2/stats/History/" # API endpoint for the Albion Online data
PRICE_URL = "http://europe.albion-online-data.com/api/v2/stats/Prices/"
#ITEMS_OF_INTEREST = get_potions() # The item you want to the the market prices for

QUALITY = '1' # Use quality 0 or 2 for non-equipment items
TIME_SCALE = str(1) # 1 = Hourly
# ======================================