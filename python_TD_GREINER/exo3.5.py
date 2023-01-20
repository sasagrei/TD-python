hDeb = int(input("Donnez l’heure de début de la location (un entier) :"))
hFin = int(input("Donnez l’heure de fin de la location (un entier) :"))
prix1 = 0
prix2 = 0
h1 = 0
h2 = 0
prixTot = 0



while (hDeb>24 or hFin>24 or hDeb<0 or hFin<0) or ((type(hDeb) or type(hFin)) != int) or (hDeb > hFin) :
    if (hDeb or hFin)>24 or (hDeb or hFin)<0:
        print("Les heures doivent être comprises entre 0 et 24 !")
    if (type(hDeb) or type(hFin)) != int:
        print("L'heure doit être donnée en entiers.")
    if hDeb == hFin:
        print("Attention ! l’heure de fin est identique à l’heure de début.\n")
    if hDeb > hFin:
        print("Attention ! le début de la location est après la fin ...\n")
    hDeb = int(input("Donnez l’heure de début de la location (un entier) :"))
    hFin = int(input("Donnez l’heure de fin de la location (un entier) :"))
    




if (7 > hDeb >= 0 and hFin<=7) or (24 > hDeb >= 17 and hFin<=24):
    for i in range(hDeb, hFin):
        prix1+=1
        h1 += 1
if (hDeb <= 7 and hFin > 7):
    for i in range(hDeb, 7):
        prix1+=1
        h1 += 1
    if hFin<18:
        for i in range(7, hFin):
            prix2+=2
            h2 += 1
    else: 
        for i in range(7, 17):
            prix2+=2
            h2 += 1
        for i in range(17, hFin):
            prix1+=1
            h1 += 1
else: 
    if hFin<18:
        for i in range(hDeb, hFin):
            prix2+=2
            h2 += 1
    else: 
        for i in range(hDeb, 17):
            prix2+=2
            h2 += 1
        for i in range(17, hFin):
            prix1+=1
            h1 += 1


prixTot = float(prix1+prix2)                                
print("Vous avez loué votre vélo pendant \n {} heure(s) au tarif horaire de 1.0 euro(s) \n {} heure(s) au tarif horaire de 2.0 euro(s) \n Le montant total à payer est de {} euro(s).".format(h1, h2, prixTot))                       