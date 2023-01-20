nbMin=int(input("Nombre minutes?"))

jour=nbMin%24
print(jour)
nbMin=nbMin//24
print(nbMin)
heure=nbMin%60
nbMin=nbMin//60
minute=nbMin%60
nbMin=nbMin//60
print("On est le {}, il est {}h{}".format(jour, heure, minute))
