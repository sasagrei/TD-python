L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
cnt = 0
nb = 0

for i in range(0, len(L1)):
    newNb = L1[i]
    newCnt = L1.count(L1[i])
    if newCnt > cnt:
        cnt = newCnt
        nb = newNb

print("Le nombre le plus frequent dans la liste est le : {} ({}x)".format(nb, cnt))
    