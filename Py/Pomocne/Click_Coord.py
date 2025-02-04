# Klik
# Kam sem to kliknul?
# https://pypi.org/project/pynput/

from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Kliknuto na souřadnice: ({x}, {y})")

# Vytvoříme posluchače myši
listener = mouse.Listener(on_click=on_click)
listener.start()

# Udržujeme skript běžící
try:
    listener.join()
except KeyboardInterrupt:
    listener.stop()


# Souřadnice:
SEARCG_bar = (638, 269)
TIER_PICK = (1010, 269)
T_ALL = (950, 300)
T_4 = (955, 406)
T_5 = (958, 430)
CENA1 = {(1072, 424), (1105, 442)} # {Levý horní roh, Pravý horní roh}
CENA2 = {(1069, 517), (1105, 533)}
CENA3 = {(1072, 605), (1105, 621)}
CENA4 = {(1072, 693), (1105, 712)}
CENA5 = {(1072, 781), (1105, 802)}
MARKET = [(651, 197),(1056, 225)]

BRIDGE_X = 2425
CAERL_X = 2526
FORT_X = 2623
LYMH_X = 2714
MARTL_X = 2805
THETF_X = 2909

MATS_START_Y = 314

# Teoreticky načíst ceny prvních pěti kvantit?