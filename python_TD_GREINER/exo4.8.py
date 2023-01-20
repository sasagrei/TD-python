dico = {'name' : 'grei', 'firstname' : 'sasa', 'promo' : 'RT1', 'group' : '21'}

print(dico)

print("Votre nom est ‘{}’, prénom est ‘{}’, vous faites partie de la promo ‘{}’ et votre groupe est ‘{}’".format(dico['name'], dico['firstname'], dico['promo'], dico['group']))

print("Les clés du dictionnaire sont :")
for key in dico.keys():
    print ("-", key)

print("Les valeurs du dictionnaire sont :")
for value in dico.values():
    print ("-", value)

print("Les tuplets du dictionnaire sont :")
for key, value in dico.items():
    print ("('{}', {})".format(key, value))