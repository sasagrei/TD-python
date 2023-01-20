nb = float(input("Vous cherchez la table de multiplication de quel nombre ? "))

for i in range(0, 10):
    print(nb, "*", i, "=", round(i*nb,1))

#print("{} * {} = {}".format(nb, i, round(i*nb, 1)))