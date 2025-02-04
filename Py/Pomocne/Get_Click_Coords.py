import pyautogui

# Počítadlo kliknutí
click_count = 0
max_clicks = 1  # Maximální počet kliknutí před ukončením

# Funkce, která zpracuje kliknutí myší
def on_click(x, y, button, pressed):
    global click_count
    if pressed:
        click_count += 1
        print(f"Kliknuto na pozici: [{x}, {y}]")
        if click_count >= max_clicks:
            print("Maximální počet kliknutí dosažen. Program končí.")
            return False  # Zastaví posluchač

# Nastavení posluchače událostí myši
import pynput.mouse

with pynput.mouse.Listener(on_click=on_click) as listener:
    listener.join()