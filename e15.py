def tizenotos():
    try:
        # Kérj be két valós számot
        a = float(input("Add meg a téglalap egyik oldalát: "))
        b = float(input("Add meg a téglalap másik oldalát: "))

        # Ellenőrizzük, hogy mindkét szám pozitív-e
        if a > 0 and b > 0:
            kerulet = 2 * (a + b)  # Kerület kiszámítása
            terulet = a * b  # Terület kiszámítása
            print(f"A téglalap kerülete: {kerulet:.2f} cm")  # Kiírás két tizedesjegyig
            print(f"A téglalap területe: {terulet:.2f} cm")  # Kiírás két tizedesjegyig
        else:
            print("Hiba: a téglalap oldalai nem pozitívak!")  # Hibaüzenet, ha nem pozitívak
    except ValueError:
        print("Hiba: Kérlek, valós számokat adj meg!")  # Hibaüzenet, ha nem számot adtak meg


# Futtatás
tizenotos()
