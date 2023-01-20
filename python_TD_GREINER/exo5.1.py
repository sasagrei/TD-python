N = []
P = []

#nb = int(input("Nombre de personnes à entrer :"))

for i in range(2):
    P.append(str(input("Votre prénom :")))
    N.append(str(input("Votre nom :")))


for j in range(2):
    if N[0] < N[1]:
        print(str.capitalize(P[j]), str.upper(N[j]))
    else:
        if N[0] == N[1]:
            if P[0] < P[1]:
                print(str.capitalize(P[j]), str.upper(N[j]))
            else: 
                P[0], P[1] = P[1], P[0]
                N[0], N[1] = N[1], N[0]
                print(str.capitalize(P[0]), str.upper(N[0]))
        else:
            N[0], N[1] = N[1], N[0]
            P[0], P[1] = P[1], P[0]
            print(str.capitalize(P[0]), str.upper(N[0]))


