# Szögtípus
def hatosfeladat():
    try:
        szog = float(input("Irj be egy számot, és megmondom hogy milyen szögtipus a beirt szögmérték alapjan:\n"))
        if 0 <= szog <= 360:
            if szog == 0 or szog == 360:
                print("Teljes szög")
            elif szog < 90:
                print("Hegyesszög")
            elif szog == 90:
                print("Derékszög")
            elif szog < 180:
                print("Tompaszög")
            elif szog == 180:
                print("Egyenesszög")
            elif szog < 360:
                print("Homorúszög")
        else:
            print("Hiba: A szög nincs a megadott tartományban!")
    except ValueError:
        print("Hiba: Nem valós számot adtál meg!")

hatosfeladat()
