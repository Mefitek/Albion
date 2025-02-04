
    search_item(m)
    time.sleep(0.5+random.random()/10)
    cena = get_avg_price()
    print(f"{int(cena)}")

print("\nELIXÍRY")

for p in pots:
    search_pot(p)
    time.sleep(0.5+random.random()/10)
    cena = get_lowest_price()
    print(f"{int(cena)}")

print() # Prázdný řádek
'''
m = "Teasel"
search_item(m)