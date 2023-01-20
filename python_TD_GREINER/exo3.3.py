import random as rdm

x = rdm.randint(0, 100)
nb = -1
tours = 0

while nb!=x:
    nb=int(input("Your guess? "))
    if nb>x:
        print("x est plus petit")
    else: 
        if nb<x:
            print("x est plus grand")
    tours+=1

print("Trouvé ! En", tours, "tours !")


