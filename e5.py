# HónapNév
def otosfeladat():
    honapok = ["Január", "Február", "Március", "Április", "Május", "Június",
               "Július", "Augusztus", "Szeptember", "Október", "November", "December"]

    try:
        szam = int(input("Irj be egy számot 1-12 kozott: \n"))  # A bemenet kezelése
        if 1 <= szam <= 12:
            print(honapok[szam - 1])  # Helyes hónap kiírása
        else:
            print("Hiba: A szám nem 1 és 12 közötti!")  # Hibaüzenet, ha nem jó a szám
    except ValueError:  # Ha nem számot adott meg a felhasználó
        print("Hiba: Nem egész számot adtál meg!")  # Hibaüzenet


otosfeladat()
