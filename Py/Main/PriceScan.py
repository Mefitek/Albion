import time
import random
import pyautogui # Screenshot
import Enums

# =================================
# ===   SCREEN COORDINATES      ===
# =================================
SEARCH_BAR = [638, 269]
RESET_FILTERS = [1335, 270]
TIER_PICK = [1010, 269]
BUY = [1273, 433]
CLOSE_BUY_LEFT = [941,313]
CLOSE_BUY_RIGHT = [1206,309]
T_ALL = [950, 300]
T_1 = [956, 325]
T_2 = [951, 354]
T_3 = [953, 381]
T_4 = [955, 406]
T_5 = [958, 430]
T_6 = [957, 464]
T_7 = [958, 489]
T_8 = [954, 516]
CENA1 = [[1072, 424], [1193, 442]] # [Levý horní roh, Pravý horní roh]
CENA2 = [[1069, 512], [1193, 530]]
CENA3 = [[1072, 605], [1193, 621]]
CENA4 = [[1072, 693], [1193, 712]]
CENA5 = [[1072, 781], [1193, 802]] # dřív místo 1193 bylo 1105
MARKET = [[651, 197],[1056, 225]]

WAIT_TIME = 1 # [s]
ingredients = Enums.get_ingrs_names_array()
pots = Enums.get_potions_array()
# =================================
# =================================

def search_item(name):
    time.sleep(random.random()/10)
    pyautogui.click(x=SEARCH_BAR[0], y=SEARCH_BAR[1])
    time.sleep(random.random()/10)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(random.random()/10)
    pyautogui.press('delete')
    time.sleep(random.random()/10)
    pyautogui.write(name)
    time.sleep(random.random()/10)
    pyautogui.press('enter')
    #time.sleep(WAIT_TIME/2+random.random()/10)
    #pyautogui.click(x=BUY[0], y=BUY[1]) # Click BUY
    #time.sleep(WAIT_TIME/2+random.random()/10)
    #pyautogui.click(x=CLOSE_BUY_LEFT[0], y=CLOSE_BUY_LEFT[1])# Close buy (position 1)
    #pyautogui.click(x=CLOSE_BUY_RIGHT[0], y=CLOSE_BUY_RIGHT[1])# Close buy (position 2)

def check_tier(curr_tier, pot_id):
    pot_tier = Enums.get_tier_from_potid(pot_id)
    if not pot_tier == curr_tier:
        # Switch to new tier
        switch_to_tier(pot_tier)
    return pot_tier

def switch_to_tier(tier):
    print(f"Switching to tier {tier}")
    time.sleep(random.random()/30)
    pyautogui.click(x=TIER_PICK[0], y=TIER_PICK[1])
    match tier:
        case '1': coords = T_1
        case '2': coords = T_2
        case '3': coords = T_3
        case '4': coords = T_4
        case '5': coords = T_5
        case '6': coords = T_6
        case '7': coords = T_7
        case '8': coords = T_8
        case _: coords = T_ALL
    time.sleep(random.random()/30)
    pyautogui.click(x = coords[0], y = coords[1])

def reset_filters():  
    time.sleep(WAIT_TIME+random.random()/10)
    pyautogui.click(x=RESET_FILTERS[0], y=RESET_FILTERS[1])

def scan_prices_ingredients():
    print("\n\nSCANNING INGREDIENT PRICES")
    reset_filters()
    for i in ingredients:
        search_item(i)
        time.sleep(WAIT_TIME+random.random()/10)

def scan_prices_potions():
    print("\n\nSCANNING POTION PRICES")
    reset_filters()
    curr_tier = 0
    for p in pots:
        curr_tier = check_tier(curr_tier, p)
        search_item(Enums.get_potion_name(p))
        time.sleep(WAIT_TIME+random.random()/10)

def scan_prices_potions_special():
    print("\n\nSCANNING POTION PRICES")
    reset_filters()
    curr_tier = 0
    for p in Enums.get_big_pots_array():
        curr_tier = check_tier(curr_tier, p)
        search_item(Enums.get_potion_name(p))
        time.sleep(WAIT_TIME+random.random()/10)

#scan_prices_potions()
#scan_prices_ingredients()