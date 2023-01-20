nMax = 3
v1 = []
v2 = []
n = 0
scal = 0.0

while n<1 or n>nMax:
    n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 3] ? "))

print("\nSaisie du premier vecteur :")
for i in range (0, n):
    v1.append(int(input("v1[{}] = ".format(i))))

print("\nSaisie du deuxième vecteur :")
for i in range (0, n):
    v2.append(int(input("v2[{}] = ".format(i))))

for i in range (0, n):
    scal += v1[i]*v2[i]

print("\nLe produit scalaire de v1 par v2 vaut ", scal)

print(type(scal))