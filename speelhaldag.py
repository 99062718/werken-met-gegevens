aantalPersonen = int(input("vul hier in met hoeveel u bent: "))
aantalVipMin = int(input("vul hier in hoeveel minuten hoe lang u in de VIP ruimte wilt: "))
aantalVIP = aantalVipMin / 5

bedrag = aantalPersonen * 7.45 + aantalVIP * aantalPersonen * 0.37

print("Dit geweldige dagje-uit met " + str(aantalPersonen) + 
" mensen in de Speelhal met " + str(aantalVIP) + " minuten VR kost je maar " 
+ str(bedrag) + " euro")