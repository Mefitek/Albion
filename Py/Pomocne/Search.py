import pyautogui
import time

def search_item(name):
    time.sleep(0.08)
    pyautogui.click(x=638, y=269) #TODO
    time.sleep(0.07)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.05)
    pyautogui.press('delete')
    time.sleep(0.07)
    pyautogui.write(name)
    time.sleep(0.06)
    pyautogui.press('enter')


# Krátké zpoždění pro případ, že potřebujete přepnout na správnou obrazovku
time.sleep(0.1)

# Kliknutí na souřadnice x=638, y=269
pyautogui.click(x=638, y=269)

# Krátké zpoždění, aby bylo jisté, že akce proběhla
time.sleep(0.1)

# Stisknutí kláves Ctrl+A (vybrat vše)
pyautogui.hotkey('ctrl', 'a')

# Krátké zpoždění
time.sleep(0.1)

# Stisknutí klávesy Delete (smazat vše)
pyautogui.press('delete')

# Krátké zpoždění
time.sleep(0.1)

# Napsání textu "burdock"
pyautogui.write('burdock')

# Krátké zpoždění
time.sleep(0.1)

# Stisknutí klávesy Enter
pyautogui.press('enter')