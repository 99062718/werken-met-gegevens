aantalPersonen = int(input("vul hier in met hoeveel u bent: "))
aantalVIP = int(input("vul hier in hoeveel minuten hoe lang u in de VIP ruimte wilt: ")) / 5

bedrag = aantalPersonen * 7.45 + aantalVIP * aantalPersonen * 0.37

print("U moet " + str(bedrag) + " betalen.")