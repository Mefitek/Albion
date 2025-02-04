import pyautogui # Screenshot
from PIL import Image # Screenshot
import pytesseract # ImageReader
from Lists import *
import time # Search
import random # Search
from Classes import *
import os # clear_console()

SAVE_SCREENS = False
PRINT = False

def my_screen(coord1, coord2, name="string1"):
    # Definujeme oblast pro screenshot (x1, y1, x2, y2)
    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]
    # Pořídíme screenshot celé obrazovky
    screenshot = pyautogui.screenshot()
    # Ořízneme obrázek na požadovanou oblast
    cropped_screenshot = screenshot.crop((x1, y1, x2, y2))
    # typ obrázku: <class 'PIL.Image.Image'>
    if SAVE_SCREENS: # Uložíme oříznutý obrázek jako screen1.jpg
        cropped_screenshot.save(name+".jpg")
        #print("Screenshot uložen jako screen1.jpg")
    return cropped_screenshot

def read_text_from_image(image: Image.Image) -> str:
    # Cesta k Tesseract executable, pokud není ve výchozí cestě
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # Přečte text z obrázku pomocí pytesseract
    text = pytesseract.image_to_string(image)
    return text

def convert_to_int(number_string):
    try:
        # Nahrazení písmenka "S" za číslici 5
        number_string = number_string.replace("S", "5")
        # Odstranění oddělovačů tisíců
        clean_string = number_string.replace(",", "")
        # Konverze na celé číslo
        number = int(clean_string)
    except ValueError:
        # V případě jakékoliv chyby vrátí 0
        number = 0
    return number

def my_sum(c1,c2,c3,c4,c5):
    ceny = []
    ceny.append(c1)
    ceny.append(c2)
    ceny.append(c3)
    ceny.append(c4)
    ceny.append(c5)
    
    sum = 0
    div = 0
    for c in ceny:
        if c != 0:
            div += 1

    if div == 0:
        avg = 0
    else:
        avg = (c1+c2+c3+c4+c5)/div

    div = 0
    for c in ceny:
        if not(c>(2*avg) or c==0):
            sum += c
            div += 1
    
    if div == 0:
        return 0
    return sum/div

def get_avg_price():
    img1 = my_screen(CENA1[0], CENA1[1], "c1")
    img2 = my_screen(CENA2[0], CENA2[1], "c2")
    img3 = my_screen(CENA3[0], CENA3[1], "c3")
    img4 = my_screen(CENA4[0], CENA4[1], "c4")
    img5 = my_screen(CENA5[0], CENA5[1], "c5")
    c1_str = read_text_from_image(img1)
    c2_str = read_text_from_image(img2)
    c3_str = read_text_from_image(img3)
    c4_str = read_text_from_image(img4)
    c5_str = read_text_from_image(img5)
    #print(f"c_str: '{c1_str}' '{c2_str}' '{c3_str}' '{c4_str}' '{c5_str}'")
    c1 = convert_to_int(c1_str)
    c2 = convert_to_int(c2_str)
    c3 = convert_to_int(c3_str)
    c4 = convert_to_int(c4_str)
    c5 = convert_to_int(c5_str)
    if PRINT: print(f"Ceny: {c1} {c2} {c3} {c4} {c5}")
    cena = my_sum(c1,c2,c3,c4,c5)
    return cena

def get_lowest_price():
    img1 = my_screen(CENA1[0], CENA1[1], "c1")
    c1_str = read_text_from_image(img1)
    c1 = convert_to_int(c1_str)
    if PRINT: print(f"Cena: {c1}")
    return c1

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

def search_pot(name):
    time.sleep(random.random()/10)
    pyautogui.click(x=SEARCH_BAR[0], y=SEARCH_BAR[1])
    time.sleep(random.random()/10)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(random.random()/10)
    pyautogui.press('delete')
    time.sleep(random.random()/10)
    pyautogui.write(name)
    # TIER
    time.sleep(random.random()/10)
    if name == "Minor Poison" or name == "Major Healing":
        pyautogui.click(x=TIER_PICK[0], y=TIER_PICK[1])
        time.sleep(random.random()/30)
        pyautogui.click(x=T_ALL[0], y=T_ALL[1])
    elif name == "Healing":
        pyautogui.click(x=TIER_PICK[0], y=TIER_PICK[1])
        time.sleep(random.random()/30)
        pyautogui.click(x=T_4[0], y=T_4[1])
    elif name == "Sticky":
        pyautogui.click(x=TIER_PICK[0], y=TIER_PICK[1])
        time.sleep(random.random()/30)
        pyautogui.click(x=T_5[0], y=T_5[1])
    
def get_city():
    img = my_screen(MARKET[0], MARKET[1], "c1")
    str = read_text_from_image(img)
    index = str.find(" Marketplace")
    if not index == -1:
        str = str[:index]
    print(f"\nMěsto: {str}")

def clear_console():
    # Pro Windows
    if os.name == 'nt':
        os.system('cls')
    # Pro Unix-based systémy
    else:
        os.system('clear')

