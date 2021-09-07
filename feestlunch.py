aantalCroissant = int(input("Geef aan hoeveel croissantjes u wilt: "))
aantalStokbrood = int(input("Geef aan hoeveel stopbroodjes u wilt: "))
aantalBon = int(input("Geef aan hoeveel cadeaubonnen u heeft: "))

bedrag = aantalCroissant * 0.39 + aantalStokbrood * 2.78 - aantalBon * 0.50

print("U moet " + str(bedrag) + " euro betalen.")