# Négyzetgyök
import math

def hetesfeladat():
    try:
        szam = float(input("Adj meg egy valós számot!:\n"))
        if szam >= 0:
            print(f"A megadott szám négyzetgyöke: {math.sqrt(szam)}")
        else:
            print("Hiba: Negatív számból nem lehet gyököt vonni!")
    except ValueError:
        print("Hiba: Nem valós számot adtál meg!")

hetesfeladat()
