L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
cnt = 0
nb = 0

for i in range(0, len(L1)):
    newNb = L1[i]
    newCnt = 0
    for j in range(0, len(L1)):
        if newNb == L1[j]:
            newCnt += 1
    if newCnt > cnt:
        cnt = newCnt
        nb = newNb

print("Le nombre le plus frequent dans la liste est le : {} ({}x)".format(nb, cnt))