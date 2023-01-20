nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
T=[]

for i in range(0, nombreEtudiants):
    note = -1
    while note < 0 or note > 20:
        note = float(input("Note étudiant {} : ".format(i)))
    T.append(note)
    moyenne += note

moyenne /= nombreEtudiants
print("\nLa moyenne de classe est ", moyenne)

print("\nNuméro de l’Etudiant | note | ecart a la moyenne")
for i in range(0, nombreEtudiants):
    ecart = moyenne - T[i]
    print("{} | {} | {}".format(i, T[i], ecart))