binome = ('login1', 'login2')
print(binome)
binome = ('login1', 'login3')
print(binome)

#del binome[1]

binomeL=list(binome)
del binomeL[1]
print(binome)
#newBinome=tuple(binomeL)
#print(newBinome)

binomeL.append('login2')
print(binome)

###
# les tuplets ne peuvent pas être modifiés avec des fonctions
#uniquement en les initialisant directement
