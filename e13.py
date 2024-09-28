import math

def tizenharmas():
    try:
        sugar = float(input("Add meg a kör sugarát:\n"))
        if sugar > 0:
            kerulet = 2 * math.pi * sugar
            terulet = math.pi * sugar ** 2
            kerekitett1 = round(kerulet, 2)
            kerekitett2 = round(terulet, 2)
            print(f"A kör kerulete: {kerekitett1} cm, \nA kör területe: {kerekitett2} cm")
        else:
            print("Hiba: a kör sugara nem pozitív!")
    except ValueError:
        print("Hiba: Nem valós számot adtál meg!")

tizenharmas()
