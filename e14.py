def tizennegyes():
    try:
        el = int(input("Add meg a kocka élének hosszát: \n"))
        if el > 0:
            felszin = 6 * el ** 2
            terfogat = el ** 3
            print(f"A kocka felszine: {felszin}\nA kocka térfogata: {terfogat}")
        else:
            print("Hiba: a kocka élének hossza nem pozitív!")
    except ValueError:
        print("Hiba: Nem egész számot adtál meg!")

tizennegyes()
