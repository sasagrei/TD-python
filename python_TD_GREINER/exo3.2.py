import time



n = int(input("Entrez en entier positif :"))

if n > 0:
    w = n
    while w >= 0:
        print(w)
        w-=1
        time.sleep(0.5)
        
    f = n
    for i in range (0,n+1):
        print(f)
        f -=1
        time.sleep(0.5)