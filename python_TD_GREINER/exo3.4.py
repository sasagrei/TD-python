i=1 
fac=1
n = -1

while n < 0:
    n = int(input("Votre nombre positif :"))

print("Tapez 1 pour utiliser while, autre pour for")

if (int(input("Choix :"))==1):
    while i<n+1:
        fac*=i
        print(fac)
        i+=1
else:
    for i in range(1, n+1):
        fac*=i
        print(fac)