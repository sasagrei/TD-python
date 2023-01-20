nb = float(input("nb heures : "))
hor = float(input("salaire : "))
sal = 0

nb2 = nb
if nb > 160:
    nb2 = 160
    nb -= 160
    nb3 = nb
    if nb > 40:
        nb3 = 40
        nb-= 40
        sal += nb*hor*1.5
    sal += nb3*(hor*1.25)
sal += nb2*hor

print(sal)