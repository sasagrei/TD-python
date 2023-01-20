jour = input("Jour?")
heure = input("Heure?")
minute = input("Minute?")

minute=int(minute)
heure=int(heure)
jour=int(jour)

if ((minute > 59) or (heure > 23) or (jour > 31)):
    print("Veuillez entrer des nombres valides.")
else: nbMin = ((jour-1)*24+(heure-1))*60+minute

print(nbMin)

