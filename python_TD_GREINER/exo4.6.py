import random as rdm

N = [5, 2, 4, 8, 1, 3]
T = [5, 2, 4, 8, 1, 3]
M = [5, 2, 4, 8, 1, 3]
#for i in range(0, rdm.randint(5,20)):
    #N.append(rdm.randint(0,9))
    #T.append(N[i])
    #TT.append(N[i])

print(N)


for i in range(0, len(N)):
    pitiNb = N[i]
    indNb = N.index(N[i])
    for j in range(i, len(N)):
        if N[j] < pitiNb:
            pitiNb = N[j]
            indNb = j
    i1=N.index(N[i])
    i2= indNb
    N[i1], N[i2] = N[i2], N[i1]
    print(N)

print()

print(sorted(T))
print(T)
M.sort()
print(M)