import pyautogui
from PIL import Image

# Definujeme oblast pro screenshot (x1, y1, x2, y2)
x1, y1, x2, y2 = 0, 0, 500, 500

# Pořídíme screenshot celé obrazovky
screenshot = pyautogui.screenshot()

# Ořízneme obrázek na požadovanou oblast
cropped_screenshot = screenshot.crop((x1, y1, x2, y2))
# typ obrázku: <class 'PIL.Image.Image'>

# Uložíme oříznutý obrázek jako screen1.jpg
cropped_screenshot.save("screen1.jpg")

print("Screenshot uložen jako screen1.jpg")
