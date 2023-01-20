import os.path
import datetime

f1 = input("fichier 1 :")
f2 = input("fichier 2 :")
time1 = 0
time2 = 0
tf1 = os.path.isfile(f1)
print(tf1)

if tf1 == True:
    time1 = os.path.getmtime(f1)
    print("La taille du fichier 1 est : ", os.path.getsize(f1), "octets.")
    
if os.path.isfile(f2) == True:
    time2 = os.path.getmtime(f2)
    print("La taille du fichier 2 est : ", os.path.getsize(f2), "octets.")
    if tf1 == True:
        if time1 > time2: 
            print("Le dernier fichier modifié est f1, à la date", datetime.datetime.fromtimestamp(time1))
        else: print("Le dernier fichier modifié est f2, à la date", datetime.datetime.fromtimestamp(time2))

