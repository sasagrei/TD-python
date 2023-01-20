BASE = 4

fromage = 800.0
eau = 2
ail = 2
pain = 400

nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))

fromage *= nbConvives/BASE
eau *= nbConvives/BASE
ail *= nbConvives/BASE
pain *= nbConvives/BASE

print("Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut :\n- {} gr de fromage\n- {} dl d'eau\n- {} gousse(s) d'ail\n- {} gr de pain".format(fromage, eau, ail, pain))
